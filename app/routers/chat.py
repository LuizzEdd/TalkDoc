from fastapi import APIRouter
from services import rag
from schemas.chats import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def ask(request: ChatRequest):
    return rag.ask_question(request.document_id, request.question)
