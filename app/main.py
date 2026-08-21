from fastapi import FastAPI
from routers import documents, chat
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
import uvicorn

app = FastAPI(title="Desafio - YAITEC")

app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(documents.router)
app.include_router(chat.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)