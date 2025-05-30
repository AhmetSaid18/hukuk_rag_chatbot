from sentence_transformers import SentenceTransformer
import torch

# Cihaz otomatik belirlenir (cuda varsa kullanır)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Model yükleniyor
model = SentenceTransformer("all-MiniLM-L6-v2", device=device)

def embed_text(texts: list[str]) -> list[list[float]]:
    """
    Embed a list of texts using SentenceTransformer.
    Returns a list of 384-dimensional vectors.
    """
    embeddings = model.encode(texts, normalize_embeddings=True)
    return embeddings.tolist()
