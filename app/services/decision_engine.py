def loan_decison(risk_score):
    if risk_score < 0.3:
        decision = "APPROVE"
    elif risk_score < 0.6:
        decision = "REVIEW"
    else:
        decision = "REJECT"
    return decision