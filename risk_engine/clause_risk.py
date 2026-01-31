RISK_RULES = {
    "High": ["sole discretion", "without notice", "in perpetuity"],
    "Medium": ["indemnify", "penalty", "liquidated damages"],
}

def score_clause(text):
    t = text.lower()
    for level, patterns in RISK_RULES.items():
        if any(p in t for p in patterns):
            return level
    return "Low"
