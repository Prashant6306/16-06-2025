from fastapi import FastAPI
from rag_pipeline import generate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG API is running"}

@app.post("/ask")
def ask_question(query: str):
    return {"response": generate_answer(query)}
