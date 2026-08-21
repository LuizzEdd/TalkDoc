from fastapi import APIRouter, UploadFile, HTTPException
from services import vectorize
from core.config import settings
import uuid

router = APIRouter(prefix = "/documents", tags=["Documentos"])

@router.post("/upload")
async def upload_document(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos.")

    document_id = str(uuid.uuid4())
    file_path = settings.UPLOAD_DIR / f"{document_id}.pdf"
    file_path.write_bytes(await file.read())

    try:
        vectorize.process_pdf(file_path, collection_name = document_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o PDF: {str(e)}")

    return {"document_id": document_id, "status": "Documento carregado e processado com sucesso."}
