import fitz  # PyMuPDF
from models.document_chunk import DocumentChunk
import uuid

def load_pdf_chunks(path: str) -> list[DocumentChunk]:
    doc = fitz.open(path)
    chunks = []
    for i, page in enumerate(doc):
        text = page.get_text()
        for paragraph in text.split("\n\n"):
            if paragraph.strip():
                chunks.append(DocumentChunk(
                    content=paragraph.strip(),
                    source=path,
                    page_number=i + 1,
                    chunk_id=str(uuid.uuid4())
                ))
    return chunks
