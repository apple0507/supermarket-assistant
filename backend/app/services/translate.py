from typing import Dict, Any
import os

_DUMMY = os.getenv("DUMMY_TRANSLATION", "1") == "1"

def translate_text(text: str, target_language: str) -> str:
    if not text:
        return text
    if _DUMMY:
        return f"[{target_language}] {text}"
    # TODO: integrate real translation provider here (e.g., DeepL, Google Cloud Translate)
    return text

def detect_language(text: str) -> str:
    # Minimal placeholder
    return "en"

def translate_product_info(product_info: Dict[str, Any], target_language: str) -> Dict[str, Any]:
    translated_info: Dict[str, Any] = {}
    for key, value in product_info.items():
        if isinstance(value, str):
            translated_info[key] = translate_text(value, target_language)
        else:
            translated_info[key] = value
    return translated_info