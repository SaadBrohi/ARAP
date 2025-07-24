# chains/answering.py

from components.llm_wrapper import LLMWrapper

class AnswerGenerator:
    def __init__(self, temperature=0.7, max_tokens=512):
        self.llm = LLMWrapper(temperature=temperature, max_tokens=max_tokens)

    def build_prompt(self, question: str, context: str, persona: str = "🎯 Precise") -> str:
        # Define style prefix per persona
        style_prompts = {
            "🎯 Precise": "You are a concise and highly accurate assistant. Provide factual answers in a formal tone.",
            "🤗 Friendly": "You are a friendly and helpful assistant. Respond in an approachable, conversational tone.",
            "🧑‍🔬 Technical": "You are a technical expert. Explain with clarity, using precise terminology and examples where relevant.",
        }

        style = style_prompts.get(persona, style_prompts["🎯 Precise"])

        return f"""{style}

Given the following context, answer the user question clearly and informatively.

Context:
{context}

Question:
{question}

Answer:"""

    def answer(self, question: str, context: str, persona: str = "🎯 Precise") -> str:
        prompt = self.build_prompt(question, context, persona)
        return self.llm.generate_answer(prompt)
