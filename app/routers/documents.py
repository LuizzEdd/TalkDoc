from fastapi import APIRouter, UploadFile, HTTPException
from services.vectorize import process_pdf, InvalidPDFError
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
        process_pdf(file_path, collection_name = document_id)
    except InvalidPDFError as e:
        file_path.unlink(missing_ok=True)
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        file_path.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail="Erro interno ao processar o documento. Tente novamente.")

    return {"document_id": document_id, "status": "Documento carregado e processado com sucesso."}
