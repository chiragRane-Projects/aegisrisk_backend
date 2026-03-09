from app.ml.explainer import explain_risk

borrower = {
    "income": 80000,
    "existing_debt": 200000,
    "employment_length": 5,
    "credit_history_years": 6,
    "delinquencies": 1
}

result = explain_risk(borrower)

print(result)