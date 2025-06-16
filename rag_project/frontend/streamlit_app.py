import streamlit as st
import requests

st.title("🧠 RAG Chatbot (FAISS + HF)")

query = st.text_input("Ask a question:")
if st.button("Ask"):
    response = requests.post("http://backend:8000/ask", params={"query": query})
    st.write(response.json()["response"])
