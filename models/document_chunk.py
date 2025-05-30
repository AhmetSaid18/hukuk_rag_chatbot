from pydantic import BaseModel

class DocumentChunk(BaseModel):
    content: str
    source: str
    page_number: int
    chunk_id: str
