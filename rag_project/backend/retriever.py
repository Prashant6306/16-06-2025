import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from utils import load_docs

embedder = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("models/faiss_index.faiss")
documents = load_docs("data/documents/")

def get_relevant_docs(query, top_k=3):
    query_vec = embedder.encode([query])
    _, I = index.search(query_vec, top_k)
    return "\n".join([documents[i] for i in I[0]])
