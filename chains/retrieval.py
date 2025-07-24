# chains/retrieval.py

from components.embedder import Embedder
from chains.vectorstore import LocalVectorStore
from typing import List

class Retriever:
    def __init__(self, persist_path: str = "vectorstore_index"):
        self.persist_path = persist_path
        self.embedder = Embedder()
        self.vector_store = LocalVectorStore(persist_path=self.persist_path)
        self.vector_store.load_index()

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        """Embeds the query and retrieves top_k matching chunks."""
        print(f"🔍 [Retriever] Embedding query: '{query}'")
        embedded_query = self.embedder.embed([query])  # This returns shape (1, dim)
        results = self.vector_store.search_with_embedding(embedded_query, top_k=top_k)

        print(f"✅ [Retriever] Retrieved {len(results)} documents.")
        return results
