from datetime import datetime
from bson import ObjectId

from app.database import borrower_collection, risk_collection
from app.ml.predictor import predict_risk


def calculate_risk(borrower_id):

    borrower = borrower_collection.find_one(
        {"_id": ObjectId(borrower_id)}
    )

    if not borrower:
        return {"error": "Borrower not found"}

    borrower["_id"] = str(borrower["_id"])

    probability = predict_risk(borrower)

    if probability < 0.3:
        category = "LOW"
    elif probability < 0.6:
        category = "MEDIUM"
    else:
        category = "HIGH"

    risk_record = {
        "borrower_id": borrower["_id"],
        "risk_score": probability,
        "risk_category": category,
        "created_at": datetime.utcnow()
    }

    result = risk_collection.insert_one(risk_record)

    risk_record["_id"] = str(result.inserted_id)

    return risk_record