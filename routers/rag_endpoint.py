from fastapi import APIRouter
from models.chat_request import ChatRequest
from services.retriever import retrieve_relevant_chunks
from services.reference_formatter import format_references
from services.openai_chat import generate_answer

router = APIRouter()

@router.post("/ask")
def ask_legal_question(request: ChatRequest):
    chunks = retrieve_relevant_chunks(request.question)
    context = format_references(chunks)
    answer = generate_answer(request.question, context)
    return {"answer": answer, "references": context}
