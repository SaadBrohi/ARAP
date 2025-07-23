# test_ingestion.py

from chains.pipeline import run_ingestion

if __name__ == "__main__":
    print("🚀 Running Document Ingestion Pipeline...")
    run_ingestion("data/")
    print("\n✅ Document ingestion completed successfully.\n")
