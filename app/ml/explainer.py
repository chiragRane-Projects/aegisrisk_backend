import shap
import joblib
import pandas as pd

from app.ml.feature_engineering import generate_features
from app.ml.dataset_builder import build_dataset

model = joblib.load("risk_model.pkl")

background_data = build_dataset()

explainer = shap.LinearExplainer(model, background_data)

def explain_risk(borrower):

    features = generate_features(borrower)

    df = pd.DataFrame([features])

    shap_values = explainer.shap_values(df)

    contributions = {}

    for i, feature in enumerate(df.columns):
        contributions[feature] = float(shap_values[0][i])

    return contributions