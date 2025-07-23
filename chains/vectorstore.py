# chains/vectorstore.py

import faiss
import numpy as np
import os
import pickle
from components.embedder import Embedder  # ✅ FIXED

class LocalVectorStore:
    def __init__(self, persist_path="data/vector_index"):
        self.embedder = Embedder()  # ✅ FIXED
        self.index_path = persist_path
        self.index = None
        self.documents = []
        self.doc_embeddings = []

    def add_documents(self, docs):
        self.documents = docs
        self.doc_embeddings = self.embedder.embed(docs)  # ✅ FIXED
        dim = self.doc_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.doc_embeddings)
        self._persist_index()

    def search(self, query, top_k=5):
        query_vec = self.embedder.embed([query]) 
        distances, indices = self.index.search(query_vec, top_k)
        results = [self.documents[i] for i in indices[0]]
        return results

    def _persist_index(self):
        if not os.path.exists(self.index_path):
            os.makedirs(self.index_path)
        faiss.write_index(self.index, os.path.join(self.index_path, "index.faiss"))
        with open(os.path.join(self.index_path, "docs.pkl"), "wb") as f:
            pickle.dump(self.documents, f)

    def load_index(self):
        index_file = os.path.join(self.index_path, "index.faiss")
        docs_file = os.path.join(self.index_path, "docs.pkl")
        if os.path.exists(index_file) and os.path.exists(docs_file):
            self.index = faiss.read_index(index_file)
            with open(docs_file, "rb") as f:
                self.documents = pickle.load(f)
            return True
        return False
