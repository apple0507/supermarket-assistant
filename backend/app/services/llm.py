from fastapi import HTTPException
import os
import base64
from collections import defaultdict
from typing import Dict, List, Any

# Azure OpenAI 配置
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "https://test-understand-images.openai.azure.com/")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "9XkEuaS5pqxayy6iMVBoMEcqEcOOoYWZxbTv5AfFOyoDBMWqu57cJQQJ99BDACi0881XJ3w3AAABACOGqWXx")
AZURE_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

_STORE: Dict[str, Dict[str, Any]] = defaultdict(lambda: {"summary": "", "turns": []})

def get_history(session_id: str) -> Dict[str, Any]:
    return _STORE[session_id]

def add_turn(session_id: str, role: str, content: Any):
    _STORE[session_id]["turns"].append({"role": role, "content": content})

def trim_with_summary(session_id: str, summarizer, max_turns: int = 8):
    hist = _STORE[session_id]
    if len(hist["turns"]) <= max_turns:
        return
    early = hist["turns"][:-max_turns]
    recent = hist["turns"][-max_turns:]
    new_summary = summarizer(early, hist.get("summary", ""))
    hist["summary"] = new_summary
    hist["turns"] = recent

def summarize_turns(early_turns: list, prev_summary: str) -> str:
    # 极简摘要占位：拼接后截断。可改为调用同模型生成高质量摘要。
    joined = prev_summary + "\n" + "\n".join(
        f'{t.get("role")}: '
        + (t["content"] if isinstance(t["content"], str) else "[multimodal content]")
        for t in early_turns
    )
    return joined[-1200:]

def chat_with_gpt(message: str = "", language: str = "auto", image_data: str = None, messages_override: list | None = None) -> str:
    """与Azure OpenAI GPT-4o对话的主要函数，支持图片输入和智能语言匹配"""
    try:
        if AZURE_API_KEY and AZURE_ENDPOINT:
            import requests
            
            url = f"{AZURE_ENDPOINT}openai/deployments/{AZURE_DEPLOYMENT}/chat/completions?api-version={AZURE_API_VERSION}"
            
            if messages_override is not None:
                messages = messages_override
            else:
                # 兼容旧用法
                user_content = []
                if message:
                    user_content.append({"type": "text", "text": message})
                if image_data:
                    base64_part = image_data.split(",")[1] if image_data.startswith("data:image") else image_data
                    user_content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_part}"}})
                system_txt = (
                    "You are a helpful supermarket shopping assistant. "
                    "Automatically respond in the user's language. "
                    "If you see an image, analyze the product and provide details."
                    if language == "auto"
                    else f"You are a helpful supermarket shopping assistant. Reply in language: {language}."
                )
                messages = [
                    {"role": "system", "content": system_txt},
                    {"role": "user", "content": user_content if len(user_content) > 1 else (user_content[0]["text"] if user_content else message)},
                ]

            payload = {
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1000,
            }
            
            # Azure OpenAI 使用 api-key 认证
            headers = {"api-key": AZURE_API_KEY, "Content-Type": "application/json"}
            
            # 发送请求到Azure OpenAI
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            return data["choices"][0]["message"]["content"].strip()

        # 没有配置时的备用响应
        return f"[Demo Mode] Azure OpenAI not configured. Your message: '{message}'"
        
    except Exception as exc:
        print(f"Azure OpenAI Error: {exc}")  # 调试用
        raise HTTPException(status_code=500, detail=f"Azure OpenAI API Error: {str(exc)}")