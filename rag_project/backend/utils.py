import os

def load_docs(path):
    docs = []
    for fname in os.listdir(path):
        with open(os.path.join(path, fname), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs
