from app.database import borrower_collection, risk_collection

def portfolio_summary():
    total_borrowers = borrower_collection.count_documents({})
    total_assessmets = risk_collection.count_documents({})
    
    return {
        "total_borrowers": total_borrowers,
        "total_risk_assessments": total_assessmets
    }
    
def risk_distribution(): 
    pipeline = [
        {
            "$group": {
                "_id": "$risk_category",
                "count": {"$sum": 1}
            }
        }
    ]
    
    results = list(risk_collection.aggregate(pipeline))
    
    distribution = {
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0
    }
    
    for r in results:
        distribution[r["_id"]] = r["count"]

    return distribution

def high_risk_borrowers():
    high_risk = list(
        risk_collection.find({"risk_category": "HIGH"})
    )
    
    borrowers = []
    
    for r in high_risk:
        borrower = borrower_collection.find_one(
            {"_id": r["borrower_id"]}
        )
        
        borrowers.append({
            "borrower_id": r["borrower_id"],
            "risk_score": r["risk_score"],
            "loan_decision": r["loan_decision"]
        })
        
    return borrowers