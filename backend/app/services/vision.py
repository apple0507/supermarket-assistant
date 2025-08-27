from fastapi import UploadFile

async def recognize_product(file: UploadFile) -> dict:
    """Minimal stub used by routers. Returns a fake recognized product.
    Replace with real OCR/vision pipeline when available.
    """
    filename = getattr(file, "filename", "uploaded-image")
    return {
        "id": "sample-123",
        "name": "Sample Product",
        "description": f"Recognized from {filename}",
    }