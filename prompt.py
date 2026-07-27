from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.

Answer the question ONLY from the given context.

If the answer is present in the context, explain it clearly.

If the answer is not present, reply:
"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
""")