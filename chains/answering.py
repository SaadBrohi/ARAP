from components.llm_wrapper import LLMWrapper

class AnswerGenerator:
    def __init__(self):
        self.llm = LLMWrapper()

    def answer(self, question: str, context: str = "") -> str:
        # Carefully designed prompt for better results
        prompt = (
            "Answer the question based on the context below. "
            "If the context does not contain enough information, answer intelligently and informatively.\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{question}\n"
        )
        return self.llm.generate_answer(prompt)
