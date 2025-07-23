from components.embedder import Embedder
from chains.vectorstore import LocalVectorStore

class Retriever:
    def __init__(self, persist_path="data/vector_index"):
        self.vector_store = LocalVectorStore(persist_path=persist_path)
        self.embedder = Embedder()
        self.vector_store.load_index()  # Ensure index is loaded

    def retrieve(self, query: str, top_k: int = 3):
        print(f"🔍 Embedding query: '{query}'")
        results = self.vector_store.search(query, top_k=top_k)  
        return results
