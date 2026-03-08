from app.ml.predictor import predict_risk

borrower = {
    "income": 80000,
    "existing_debt": 200000,
    "employment_length": 5,
    "credit_history_years": 6,
    "delinquencies": 1
}

score = predict_risk(borrower)

print("Default probability:", score)