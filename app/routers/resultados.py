from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
from app.schemas import Usuario, MostarUsuario, ActualizarUsuario
from app.db.database import get_db
from app.repository import user
from app.oauth import get_current_user
from PIL import Image, ImageDraw, ImageFont
import shutil
import os
UPLOAD_DIR = "uploaded_images"
EDITED_DIR = "edited_images"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
if not os.path.exists(EDITED_DIR):
    os.makedirs(EDITED_DIR)
    
router = APIRouter(
    prefix="/resultados",
    tags=["Resultados"]
)
@router.post("/upload_images/", status_code=status.HTTP_201_CREATED)
async def upload_images(files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    file_locations = []
    edited_file_locations = []
    results = []

    for idx, file in enumerate(files):
        file_location = f"{UPLOAD_DIR}/{file.filename}"
        edited_file_location = f"{EDITED_DIR}/edited_{file.filename}"
        
        # Guardar la imagen original
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        
        # Editar la imagen usando Pillow
        with Image.open(file_location) as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            draw.text((10, 10), f"Resultado {idx + 1}", font=font, fill="white")
            img.save(edited_file_location)

        file_locations.append(file_location)
        edited_file_locations.append(edited_file_location)
        results.append(f"Resultado {idx + 1}: {20 * (idx + 1)}")

    return {
        "info": "Archivos subidos exitosamente",
        "results": results,
        "file_paths": file_locations,
        "edited_file_paths": edited_file_locations
    }