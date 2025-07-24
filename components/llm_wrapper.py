import os
from llama_cpp import Llama

class LLMWrapper:
    def __init__(self):
        model_path = "models/Phi-3-mini-4k-instruct.Q4_0.gguf"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model file not found at: {model_path}. Please ensure it's correctly placed.")

        print(f"🔗 Loading Phi-3 from: {model_path}")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=4,
            n_gpu_layers=0,  # CPU-only
            verbose=False
        )
        print("✅ Phi-3 model loaded successfully.")

    def generate_answer(self, prompt: str) -> str:
        print("🧠 Generating answer...\n")
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers clearly, concisely, and intelligently."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512,
        )
        return response["choices"][0]["message"]["content"].strip()
