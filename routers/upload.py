from fastapi import APIRouter, UploadFile, File
from services.pdf_processor import process_pdf
import os

router = APIRouter()


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    save_path = os.path.join("data/pdfs", file.filename)
    with open(save_path, "wb") as f:
        f.write(await file.read())

    process_pdf(save_path)  # işleme gönder
    return {"message": f"{file.filename} yüklendi ve işlendi"}
