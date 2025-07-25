# 📚 QueryVerse — Local LLM-Powered Document QA System

QueryVerse is a fully local, intelligent question-answering system that enables users to interact with their own documents using natural language. It combines local embedding models, a retrieval-augmented generation (RAG) pipeline, and a locally hosted LLM (Phi-3) to deliver fast, private, and context-aware answers — optionally enhanced with real-time web results.

> ⚙️ Powered by `Phi-3-mini-4k-instruct` (via llama-cpp), FAISS, and SentenceTransformers — no internet or external APIs required (unless web search is enabled).

---

## 🔧 Features

- 📄 **Multi-document support**: Upload PDFs or text files and ask questions across them.
- 🧠 **Local vector search**: Uses FAISS with sentence-transformer embeddings for efficient semantic retrieval.
- 🤖 **LLM response generation**: Uses a locally hosted Phi-3 model for natural and informative answers.
- 🎭 **Persona selection**: Choose between *Precise*, *Friendly*, and *Technical* assistant styles.
- 🌐 **Optional web augmentation**: If enabled, SerpAPI provides real-time web search integration.
- 💬 **Chat memory**: Maintains and displays the last 10 conversations for context and continuity.
- 🎨 **Modern UI**: Built with Streamlit and styled for a sleek, dark, and conversational interface.


---

## 🚀 Getting Started

### 1. 📥 Install Requirements

pip install -r requirements.txt

### 2. 🧠 Download LLM & Embedding Model

Place the Phi-3-mini-4k-instruct.Q4_0.gguf in models/

Place the all-mpnet-base-v2 folder in models/ if running locally, or use it from HuggingFace.

### 3. 🔐 (Optional) Set SerpAPI Key

If using web search:

export SERPAPI_API_KEY="your_api_key_here"

---


### 💡 How It Works

Upload Documents → Stored in uploaded_docs/

Run Ingestion → Extract text, split into chunks, embed, and index with FAISS

Ask a Question → Embed query, retrieve top k relevant chunks

Generate Answer → Feed question + context to LLM, render with persona

Optional Web Search → Appends SerpAPI results into LLM prompt

---

### ⚙️ Configuration

Chunking: 250 tokens with 40 overlap

LLM Context Window: 4096 tokens

Max Tokens per Response: 512

FAISS Vector Index: Saved to vectorstore_index/

---

### Tech Stack

| Component      | Tech/Library                           |
| -------------- | -------------------------------------- |
| Embeddings     | SentenceTransformers (`mpnet-base-v2`) |
| Vector Search  | FAISS                                  |
| LLM            | Phi-3 via `llama-cpp-python`           |
| Web Search     | SerpAPI (Google engine)                |
| UI             | Streamlit + Custom CSS                 |
| Text Splitting | LangChain                              |


### 🔒 Privacy First
All processing — including embedding and LLM inference — runs locally on your machine. No data leaves your device unless you explicitly enable web search.


### 🙌 Credits
Built with 💻 by Saad Brohi
Inspired by the power of retrieval-augmented generation, this project reflects a local-first, privacy-respecting approach to conversational AI.

### 📄 License
MIT License — use it, improve it, and contribute back.



