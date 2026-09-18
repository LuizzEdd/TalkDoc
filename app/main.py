from fastapi import FastAPI
from routers import documents, chat
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
import uvicorn
from fastapi import Request
from fastapi.responses import JSONResponse
import logging

app = FastAPI(title="Projeto Talkdoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(documents.router)
app.include_router(chat.router)

logger = logging.getLogger("talkdoc")

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Erro não tratado") 
    return JSONResponse(
        status_code=500,
        content={"detail": "Ocorreu um erro interno. Tente novamente mais tarde."}
    )