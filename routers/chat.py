from fastapi import APIRouter
from pydantic import BaseModel
from services.vector_store import query_vector_store
from services.llm_service import ask_llm

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(request: ChatRequest):
    docs = query_vector_store(request.question)
    answer = ask_llm(docs, request.question)
    return {"answer": answer}
