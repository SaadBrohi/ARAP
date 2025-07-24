# components/loader.py

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from typing import List
import os

SUPPORTED_EXTENSIONS = [".pdf", ".txt"]

def load_documents_from_folder(folder_path: str) -> List[str]:
    """
    Loads and splits documents from the given folder into clean chunks.
    Supports PDF and TXT files.
    """
    docs = []
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"❌ Folder '{folder_path}' not found or not a directory.")

    for file in folder.glob("*"):
        ext = file.suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            print(f"⚠️ Skipping unsupported file: {file.name}")
            continue

        try:
            loader = (
                PyPDFLoader(str(file))
                if ext == ".pdf"
                else TextLoader(str(file))
            )

            loaded_docs = loader.load()
            docs.extend(loaded_docs)
            print(f"✅ Loaded: {file.name} ({len(loaded_docs)} chunks)")

        except Exception as e:
            print(f"❌ Failed to load '{file.name}': {e}")

    if not docs:
        print("⚠️ No documents loaded.")
        return []

    # 📎 Split text into semantically coherent chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=40,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    split_docs = splitter.split_documents(docs)
    print(f"🧩 Total chunks after splitting: {len(split_docs)}")

    return split_docs
