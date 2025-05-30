from services.embedder import embed_text
from services.store_provider import faiss_store


def retrieve_relevant_chunks(question: str) -> list:
    query_embedding = embed_text([question])[0]
    return faiss_store.search(query_embedding, k=3)
