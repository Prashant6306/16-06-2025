from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from backend.utils import load_docs

docs = load_docs("backend/data/documents")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
faiss.write_index(index, "backend/models/faiss_index.faiss")
