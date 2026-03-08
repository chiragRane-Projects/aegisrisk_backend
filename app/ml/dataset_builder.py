import pandas as pd
from app.database import borrower_collection
from app.ml.feature_engineering import generate_features

def build_dataset():
    records = []
    
    borrowers = borrower_collection.find()
    
    for b in borrowers:
        
        features = generate_features(b)
        
        record = {
            "debt_to_income": features["debt_to_income"],
            "income_stability": features["income_stability"],
            "credit_maturity": features["credit_maturity"],
            "delinquency_ratio": features["delinquency_ratio"]
        }
        
        records.append(record)
    
    df = pd.DataFrame(records)
    
    return df