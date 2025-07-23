
from chains.retrieval import Retriever

if __name__ == "__main__":
    retriever = Retriever(persist_path="data/vector_index")
    
    query = input("\n🧠 Enter your question: ")
    results = retriever.retrieve(query, top_k=3)

    print("\n🔎 Top Results:")
    for i, doc in enumerate(results, 1):
     print(f"\n--- Result #{i} ---\n{doc.strip()}")

