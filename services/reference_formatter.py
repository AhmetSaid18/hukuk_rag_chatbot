from models.document_chunk import DocumentChunk

def format_references(chunks: list[DocumentChunk]) -> list[str]:
    return [
        f"{chunk.content.strip()} (source: {chunk.source.split('/')[-1]}, page: {chunk.page_number})"
        for chunk in chunks
    ]
