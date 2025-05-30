import faiss
import numpy as np
from models.document_chunk import DocumentChunk

class FaissStore:
    def __init__(self, embedding_dim=384):  # SentenceTransformer MiniLM için 384
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def add(self, embeddings: list[list[float]], chunks: list[DocumentChunk]):
        np_embeddings = np.array(embeddings).astype("float32")
        self.index.add(np_embeddings)
        self.metadata.extend(chunks)

    def search(self, query_embedding: list[float], k=3) -> list[DocumentChunk]:
        D, I = self.index.search(np.array([query_embedding]).astype("float32"), k)
        return [self.metadata[i] for i in I[0] if i < len(self.metadata)]
