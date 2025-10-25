BLOCK_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass policy",
]


def is_blocked(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in BLOCK_PATTERNS)
