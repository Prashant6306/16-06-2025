from retriever import get_relevant_docs
from transformers import pipeline

qa_model = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")

def generate_answer(query):
    context = get_relevant_docs(query)
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    response = qa_model(prompt, max_new_tokens=100)[0]["generated_text"]
    return response
