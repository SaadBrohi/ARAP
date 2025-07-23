from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class LLMWrapper:
    def __init__(self, model_name: str = "google/flan-t5-base"):
        print(f"🔗 Loading Hugging Face LLM: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=-1  # -1 means CPU
        )
        print("✅ Model loaded and ready.")

    def generate_answer(self, prompt: str, max_length: int = 256) -> str:
        if not prompt.strip():
            return "❗ Empty prompt provided."
        
        result = self.pipeline(prompt, max_length=max_length, do_sample=False)
        return result[0].get('generated_text', '').strip()
