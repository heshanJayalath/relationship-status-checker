import re
from config import TEXT_KEYWORDS

def text_score(text: str) -> int:
    score = 0
    text = text.lower()
    for word, pts in TEXT_KEYWORDS.items():
        if re.search(rf"\b{word}\b", text):
            score += pts
    return score

def analyze_bio_and_captions(bio: str, captions: list) -> int:
    total = text_score(bio)
    for cap in captions:
        total += text_score(cap)
    return total