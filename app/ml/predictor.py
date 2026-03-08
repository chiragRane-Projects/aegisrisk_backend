import joblib
import pandas as pd

from app.ml.feature_engineering import generate_features

model = joblib.load("risk_model.pkl")

def predict_risk(borrower):
    features = generate_features(borrower)
    df = pd.DataFrame([features])
    probability = model.predict_proba(df)[0][1]
    return probability