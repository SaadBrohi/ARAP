# chains/pipeline.py

from components.loader import load_documents_from_folder
from chains.vectorstore import LocalVectorStore

def run_ingestion(folder_path: str, persist_path: str = "data/vector_index"):
    # Step 1: Load & split documents
    print(f"📄 Loading documents from {folder_path}...")
    documents = load_documents_from_folder(folder_path)
    print(f"✅ Loaded {len(documents)} document chunks.")

    # Step 2: Initialize vector store
    vector_store = LocalVectorStore(persist_path=persist_path)

    # Step 3: Add and index documents
    print(f"🧠 Embedding and indexing documents...")
    vector_store.add_documents([doc.page_content for doc in documents])
    print(f"✅ Indexing complete and persisted at {persist_path}.")

if __name__ == "__main__":
    run_ingestion("data/")
