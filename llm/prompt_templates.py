def clause_prompt(clause, risk, ctype):
    return f"""
You are a legal assistant for Indian SME business owners.

Clause:
{clause}

Detected:
- Type: {ctype}
- Risk: {risk}

Explain in simple business English.
Explain why risky.
Suggest a safer alternative clause.
Give negotiation advice.
Avoid legal jargon.
"""
