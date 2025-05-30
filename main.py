from fastapi import FastAPI
from routers.rag_endpoint import router
from services.pdf_loader import load_pdf_chunks
from services.embedder import embed_text
from vectorstore.faiss_store import FaissStore
import os
import uvicorn
from services.store_provider import faiss_store
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(router)

# Global FAISS store
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için istersek "http://localhost:5500" gibi sınırlarız
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    pdf_dir = "data/pdfs/"
    all_chunks = []

    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            chunks = load_pdf_chunks(os.path.join(pdf_dir, file))
            all_chunks.extend(chunks)

    embeddings = embed_text([chunk.content for chunk in all_chunks])
    faiss_store.add(embeddings, all_chunks)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5300, reload=True)
