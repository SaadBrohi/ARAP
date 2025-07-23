from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

def load_documents_from_folder(folder_path: str):
  
    docs = []
    folder = Path(folder_path)

    for file in folder.glob("*"):
        if file.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file))
        elif file.suffix.lower() == ".txt":
            loader = TextLoader(str(file))
        else:
            print(f"Unsupported file format: {file.name}")
            continue

        loaded = loader.load()
        docs.extend(loaded)

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    split_docs = splitter.split_documents(docs)
    return split_docs
