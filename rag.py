from typing import TypedDict

from pinecone import Pinecone

from langgraph.graph import StateGraph, END

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
)

from prompt import prompt

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX_NAME)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings,
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)



llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0,
)

class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    score: float



def retrieve(state):

    docs = retriever.invoke(state["question"])

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return {
        "context": context,
        "score": len(docs)
    }


def generate(state):

    chain = prompt | llm

    response = chain.invoke({
        "context": state["context"],
        "question": state["question"]
    })

    return {
        "answer": response.content
    }



graph = StateGraph(GraphState)

graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)

graph.set_entry_point("retrieve")

graph.add_edge("retrieve", "generate")

graph.add_edge("generate", END)

app = graph.compile()


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    result = app.invoke({
        "question": question,
        "context": context
    })

    return {
        "answer": result["answer"],
        "context": [doc.page_content for doc in docs],
        "score": 0.95
    }