from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from rag import ask_question

app = FastAPI(title="Agentic AI RAG Chatbot")

app.mount("/static", StaticFiles(directory="templates"), name="static")

class ChatRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(request: ChatRequest):
    return ask_question(request.question)