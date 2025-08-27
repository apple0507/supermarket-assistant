from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.services.llm import chat_with_gpt, summarize_turns
from app.utils.memory import get_history, add_turn, trim_with_summary
from app.services.vision import recognize_product

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    language: str = "auto"
    image_data: Optional[str] = None
    session_id: Optional[str] = None  # optional

@router.post("/chat")
async def chat(request: ChatRequest):
    sid = request.session_id or "default"  # fallback
    hist = get_history(sid)

    system_msg = {
        "role": "system",
        "content": "You are a helpful supermarket assistant. Always reply in the user's language.",
    }

    messages = [system_msg]

    if hist.get("summary"):
        messages.append({"role": "system", "content": f"[CONTEXT SUMMARY]\n{hist['summary']}"})

    # 追加历史近几轮
    messages.extend(hist["turns"])

    # 当前用户消息（可多模态）
    user_content = []
    if request.message:
        user_content.append({"type": "text", "text": request.message})
    if request.image_data:
        base64_part = request.image_data.split(",")[1] if request.image_data.startswith("data:image") else request.image_data
        user_content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_part}"}})

    messages.append({
        "role": "user",
        "content": user_content if len(user_content) > 1 else (user_content[0]["text"] if user_content else request.message),
    })

    # 调用 LLM
    resp = chat_with_gpt(messages_override=messages)

    # 写入记忆
    add_turn(sid, "user", messages[-1]["content"])
    add_turn(sid, "assistant", resp)

    # 滚动摘要
    trim_with_summary(sid, summarize_turns, max_turns=8)

    return {"response": resp}

@router.post("/upload")
async def upload_image(file: UploadFile = File(...), language: str = "en"):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    product_info = await recognize_product(file)
    if not product_info:
        raise HTTPException(status_code=404, detail="Product not recognized")
    
    # Assuming translate_text is defined elsewhere or will be added
    # translated_info = translate_text(product_info['description'], language)
    return {
        "product": product_info,
        # "translated_description": translated_info # This line was commented out in the original file
    }