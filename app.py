import os
import streamlit as st
from chains.pipeline import run_ingestion
from chains.retrieval import Retriever
from chains.answering import AnswerGenerator
from utils.history import load_history, save_to_history
from utils.ui_components import render_chat_bubble
from utils.prompt_styles import SYSTEM_PROMPTS
from components.web_search import web_search

# --- Streamlit UI Setup ---
st.set_page_config(page_title="QueryVerse", layout="wide")

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📚 QueryVerse — Ask Anything from Your Docs or Web")

# --- Sidebar: Document Upload ---
with st.sidebar:
    st.header("📂 Upload Files")

    os.makedirs("uploaded_docs", exist_ok=True)
    os.makedirs("vectorstore_index", exist_ok=True)

    existing_docs = os.listdir("uploaded_docs")
    indexed_files = set(os.listdir("vectorstore_index"))
    new_files_uploaded = False

    uploaded_files = st.file_uploader("Choose PDF or text files", type=["pdf", "txt"], accept_multiple_files=True)

    if uploaded_files:
        new_files_uploaded = True
        for file in uploaded_files:
            file_path = os.path.join("uploaded_docs", file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
        st.success("✅ New files uploaded successfully.")

    if existing_docs:
        st.markdown("### 📄 Existing Uploaded Files")
        for doc in existing_docs:
            st.markdown(f"- {doc}")
    else:
        st.info("📭 No documents uploaded yet.")

    st.header("🌐 Web Search (Optional)")
    use_web = st.checkbox("Enable web search", value=False)

    st.header("🧠 Assistant Style")
    persona = st.radio("Select a persona", ["🎯 Precise", "🤗 Friendly", "🧑‍🔬 Technical"])

# --- Session State Init ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_history()

if "retriever" not in st.session_state:
    st.session_state.retriever = Retriever()

if "answer_generator" not in st.session_state:
    st.session_state.answer_generator = AnswerGenerator()

# --- Ingest Only New Files ---
if new_files_uploaded:
    run_ingestion("uploaded_docs", "vectorstore_index")
    st.success("✅ Files ingested and indexed!")

elif existing_docs:
    if not os.listdir("vectorstore_index"):
        run_ingestion("uploaded_docs", "vectorstore_index")
        st.info("ℹ️ Existing uploaded documents have been loaded into index.")
    else:
        st.info("📁 Using previously indexed documents. No ingestion needed.")

# --- Main Chat Interface ---
question = st.text_input("💬 Ask your question:")

if st.button("Ask") and question:
    with st.spinner("🤖 Thinking..."):
        # Retrieve context
        context = st.session_state.retriever.retrieve(question)

        # Optional web search
        if use_web:
            web_result = web_search(question)
            context += f"\n[Web]: {web_result}"

        # Use system prompt based on persona
        persona_key = {
            "🎯 Precise": "Formal",
            "🤗 Friendly": "Friendly",
            "🧑‍🔬 Technical": "Technical"
        }.get(persona, "Formal")

        system_prompt = SYSTEM_PROMPTS.get(persona_key, "")
        full_prompt = st.session_state.answer_generator.build_prompt(question, context, persona)

        answer = st.session_state.answer_generator.llm.generate_answer(full_prompt)

        # Save to session and disk
        st.session_state.chat_history.append({"question": question, "answer": answer})
        save_to_history(question, answer)

# --- Display Chat History ---
st.markdown("### 🧾 Chat History")
for chat in reversed(st.session_state.chat_history[-10:]):
    render_chat_bubble("user", chat["question"])
    render_chat_bubble("bot", chat["answer"])
