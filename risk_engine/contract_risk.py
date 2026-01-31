def contract_score(clause_scores):
    mapping = {"Low":1, "Medium":2, "High":3}
    total = sum(mapping[s] for s in clause_scores)
    avg = total / len(clause_scores)

    if avg < 1.6:
        return "Low Risk"
    elif avg < 2.4:
        return "Medium Risk"
    return "High Risk"
