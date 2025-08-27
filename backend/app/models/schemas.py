from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    name: str
    description: str
    image_url: str
    suitable_pairings: List[str]
    suitable_for: List[str]

class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: str

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    target_language: str

class ProductInfoResponse(BaseModel):
    product: Product
    translations: Optional[List[TranslationResponse]] = None

class ChatResponse(BaseModel):
    messages: List[ChatMessage]