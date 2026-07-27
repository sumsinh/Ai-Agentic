# AI Engineer Interview Task - RAG Chatbot

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Python, LangGraph, Pinecone, Hugging Face Embeddings, Groq LLM, and FastAPI.

The chatbot answers user questions strictly based on the provided **Agentic AI eBook**.

---

## Tech Stack

- Python
- FastAPI
- LangGraph
- Pinecone
- Hugging Face Embeddings
- Groq
- LangChain

---

## Features

- PDF Loading
- Text Chunking
- Vector Embeddings
- Pinecone Vector Database
- LangGraph Workflow
- Context-Based Question Answering
- Retrieved Context Chunks
- Confidence Score
- FastAPI REST API
- Simple Chat UI

---

## Project Structure

```
ai-rag-chatbot/
│
├── data/
│   └── Ebook-Agentic-AI.pdf
│
├── templates/
│   └── index.html
│
├── app.py
├── config.py
├── ingest.py
├── prompt.py
├── rag.py
├── test.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## Architecture

```
                User Question
                     │
                     ▼
              FastAPI Endpoint
                     │
                     ▼
               LangGraph Flow
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Pinecone Retriever      Groq LLM
          │                     ▲
          ▼                     │
   HuggingFace Embeddings       │
          ▲                     │
          │                     │
          PDF → Chunking → Embeddings
                     │
                     ▼
                 Pinecone DB
```

---

## Installation

```bash
git clone <repository>

cd ai-rag-chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Configure

Create a `.env` file.

```
PINECONE_API_KEY=your_key

PINECONE_INDEX_NAME=agentic-ai

GROQ_API_KEY=your_key
```

---

## Index the PDF

```bash
python ingest.py
```

---

## Run

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## Sample Questions

- What is Agentic AI?
- What are Autonomous Agents?
- Explain the components of Agentic AI.
- What is the role of Memory in Agentic AI?
- What are Multi-Agent Systems?
- What are the applications of Agentic AI?

---

## API

POST

```
/chat
```

Request

```json
{
    "question":"What is Agentic AI?"
}
```

Response

```json
{
    "answer":"...",
    "context":[...],
    "score":0.95
}
```