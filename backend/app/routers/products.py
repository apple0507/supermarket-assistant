from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import product_info, vision, translate

router = APIRouter()

@router.post("/products/upload")
async def upload_product_image(file: UploadFile = File(...)):
    try:
        product_details = await vision.recognize_product(file)
        return product_details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/products/{product_id}")
async def get_product_info(product_id: str, lang: str = "en"):
    try:
        product_details = await product_info.get_product_details(product_id)
        translated_info = await translate.translate_product_info(product_details, lang)
        return translated_info
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))