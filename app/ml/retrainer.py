import joblib
from datetime import datetime
from sklearn.linear_model import LogisticRegression

from app.ml.dataset_builder import build_dataset
from app.database import db

def create_labels(df):
    df["default"] = (
        (df["debt_to_income"] > 2) |
        (df["delinquency_ratio"] > 0.2)
    ).astype(int)

    return df

def retrain_model():
    df = build_dataset()

    df = create_labels(df)

    X = df[
        [
            "debt_to_income",
            "income_stability",
            "credit_maturity",
            "delinquency_ratio",
        ]
    ]

    y = df["default"]

    model = LogisticRegression()

    model.fit(X, y)

    joblib.dump(model, "risk_model.pkl")

    model_versions = db["model_versions"]

    record = {
        "model_type": "LogisticRegression",
        "trained_on_records": len(df),
        "trained_at": datetime.utcnow(),
    }

    result = model_versions.insert_one(record)

    record["_id"] = str(result.inserted_id)

    return record