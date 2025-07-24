# chains/vectorstore.py

import os
import faiss
import pickle
import numpy as np
from components.embedder import Embedder

class LocalVectorStore:
    def __init__(self, persist_path="data/vector_index"):
        self.persist_path = persist_path
        self.index = None
        self.documents = []
        self.embedder = Embedder()
        self.dim = None

    def add_documents(self, docs):
        """Embed and index documents."""
        self.documents = docs
        embeddings = self.embedder.embed(docs)
        self.dim = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(self.dim)
        self.index.add(embeddings)

        self._persist_index()
        self._persist_documents()

    def search_with_embedding(self, query_vec, top_k=5):
        """Run similarity search on pre-embedded query vector."""
        if not self.index:
            raise ValueError("Index not loaded or initialized.")
        distances, indices = self.index.search(query_vec, top_k)
        results = [self.documents[i] for i in indices[0]]
        return results

    def _persist_index(self):
        os.makedirs(self.persist_path, exist_ok=True)
        index_file = os.path.join(self.persist_path, "index.faiss")
        faiss.write_index(self.index, index_file)

    def _persist_documents(self):
        docs_file = os.path.join(self.persist_path, "docs.pkl")
        with open(docs_file, "wb") as f:
            pickle.dump(self.documents, f)

    def load_index(self):
        index_file = os.path.join(self.persist_path, "index.faiss")
        docs_file = os.path.join(self.persist_path, "docs.pkl")

        if os.path.exists(index_file) and os.path.exists(docs_file):
            self.index = faiss.read_index(index_file)
            with open(docs_file, "rb") as f:
                self.documents = pickle.load(f)
            self.dim = self.index.d
            return True
        return False
