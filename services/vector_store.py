import os
from langchain.embeddings import HuggingFaceEmbeddings  # OpenAIEmbeddings yerine transformers embedding
from langchain_community.vectorstores import FAISS

DB_PATH = "data/faiss_index"


def add_to_vector_store(chunks):
    # Transformer tabanlı embedding oluştur. "all-mpnet-base-v2" modeli önerilir.
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")

    if os.path.exists(DB_PATH):
        db = FAISS.load_local(DB_PATH, embeddings)
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)

    db.save_local(DB_PATH)


def query_vector_store(query: str, k=4):
    # Her sorguda embedding oluşturuluyor, aynı model kullanılabilir.
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    db = FAISS.load_local(DB_PATH, embeddings)
    return db.similarity_search(query, k=k)
