from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    CHAT_MODEL: str = "gemini-3.5-flash"
    EMBEDDING_MODEL: str = "models/gemini-embedding-001"

    UPLOAD_DIR: Path = BASE_DIR / "storage" / "uploads"
    CHROMA_DIR: Path = BASE_DIR / "storage" / "chroma_db"

    CORS_ORIGINS: str = "http://localhost:5173"

    @property
    def cors_origins_list(self) -> list[str]:
        return self.CORS_ORIGINS.split(",")

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    TOP_K: int = 5

    class Config:
        env_file = BASE_DIR / "keys.env"

settings = Settings()

settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
settings.CHROMA_DIR.mkdir(parents=True, exist_ok=True)