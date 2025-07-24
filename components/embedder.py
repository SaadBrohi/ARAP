# components/embedder.py

from sentence_transformers import SentenceTransformer
import os
import torch

class Embedder:
    def __init__(self, model_name=None):
        """
        Loads a local or HuggingFace embedding model safely.
        Avoids meta tensor errors by not using .to() on SentenceTransformer.
        """
        default_model = "sentence-transformers/all-mpnet-base-v2"
        local_model_path = "models/all-mpnet-base-v2"

        self.model_name = model_name or (local_model_path if os.path.exists(local_model_path) else default_model)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"🔗 Loading embedding model: {self.model_name} on {self.device}")

        self.model = SentenceTransformer(self.model_name)
        self.model.eval()  # Optional: disables dropout, etc.

    def embed(self, texts: list[str]):
        """
        Converts a list of texts into dense vector embeddings.
        """
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            device=self.device  # Proper way to use device in SentenceTransformer
        )
