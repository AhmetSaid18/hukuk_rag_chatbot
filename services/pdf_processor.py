import os

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from services.vector_store import add_to_vector_store


def process_pdf(filepath: str):
    from langchain.schema.document import Document
    loader = PyMuPDFLoader(filepath)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # Metadata ekleyelim: filename
    for chunk in chunks:
        chunk.metadata["source"] = os.path.basename(filepath)  # sadece dosya adı

    add_to_vector_store(chunks)
