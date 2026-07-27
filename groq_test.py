from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)