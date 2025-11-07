from difflib import SequenceMatcher

def check_similarity(code1: str, code2: str):
    ratio = SequenceMatcher(None, code1, code2).ratio()
    return round(ratio * 100, 2)
