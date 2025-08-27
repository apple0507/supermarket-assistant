from collections import defaultdict
from typing import Dict, Any

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
