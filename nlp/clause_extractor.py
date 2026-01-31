import re

def extract_clauses(text):
    pattern = r"\n\d+\.|\n[A-Z][A-Z\s]{3,}:"
    clauses = re.split(pattern, text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]
