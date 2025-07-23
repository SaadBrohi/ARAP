from components.llm_wrapper import LLMWrapper

class AnswerGenerator:
    def __init__(self):
        self.llm = LLMWrapper()

    def answer(self, question: str, context: str = "") -> str:
        if not question.strip():
            return "❗ Question cannot be empty."

        prompt = f"""
You are a helpful AI assistant. Use the context below to answer the question clearly.

📚 Context:
{context}

❓ Question:
{question}

🧠 Answer:"""

        return self.llm.generate_answer(prompt)
