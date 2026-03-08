import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from app.ml.synthetic_data import generate_synthetic_borrowers

def create_labels(df):
    df["default"] = (
        (df["debt_to_income"] > 2) | (df["delinquency_ratio"] > 0.2)
    ).astype(int)
    
    return df

def train_model():
    df = generate_synthetic_borrowers()
    
    df = create_labels(df)
    
    X = df[[
        "debt_to_income",
        "income_stability",
        "credit_maturity",
        "delinquency_ratio"
    ]]
    
    y = df["default"]
    
    model = LogisticRegression()
    
    model.fit(X, y)
    
    joblib.dump(model, "risk_model.pkl")
    
    print("Model trained and saved")
    
if __name__ == "__main__":
    train_model()