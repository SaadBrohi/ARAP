import os
from llama_cpp import Llama

class LLMWrapper:
    def __init__(self, temperature=0.7, max_tokens=512):
        self.temperature = temperature
        self.max_tokens = max_tokens
        model_path = "models/Phi-3-mini-4k-instruct.Q4_0.gguf"

        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"❌ Model not found at: {model_path}. Please ensure it's placed correctly."
            )

        print(f"🔗 Loading Phi-3 model from: {model_path}")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=4,
            n_gpu_layers=0,
            verbose=False
        )
        print("✅ Phi-3 model loaded successfully.")

    def generate_answer(self, prompt: str) -> str:
        """
        Generates a response from the Phi-3 model using a full prompt string.
        Assumes the prompt is already constructed (e.g., by AnswerGenerator).
        """
        print("🧠 Generating with Phi-3 model...")
        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant who answers clearly, concisely, and intelligently."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response["choices"][0]["message"]["content"].strip()
