AMBIGUOUS_TERMS = [
    "reasonable",
    "as may be determined",
    "from time to time",
    "at sole discretion"
]

def detect_ambiguity(text):
    return any(term in text.lower() for term in AMBIGUOUS_TERMS)
