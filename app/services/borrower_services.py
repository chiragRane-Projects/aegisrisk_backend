from app.database import borrower_collection
from bson import ObjectId
from app.ml.retrainer import retrain_model

def get_borrower_data(borrower_id):
    borrower = borrower_collection.find_one({"_id": ObjectId(borrower_id)})
    
    if borrower:
        borrower["_id"] = str(borrower["_id"])
        
    return borrower

def get_all_borrowers():
    borrowers = []
    
    for b in borrower_collection.find():
        b["_id"] = str(b["_id"])
        borrowers.append(b)
        
    return borrowers

def create_borrower(data):
    borrower = {
        "name": data.name,
        "age": data.age,
        "income": data.income,
        "employment_length": data.employment_length,
        "existing_debt": data.existing_debt,
        "credit_history_years": data.credit_history_years,
        "delinquencies": data.delinquencies
    }

    result = borrower_collection.insert_one(borrower)
    total_borrowers = borrower_collection.count_documents({})
    
    if total_borrowers % 50 == 0:
        retrain_model()
    
    borrower["_id"] = str(result.inserted_id)

    return borrower

def update_borrower_data(borrower_id, data):
    update_data = {
        "name": data.name,
        "age": data.age,
        "income": data.income,
        "employment_length": data.employment_length,
        "existing_debt": data.existing_debt,
        "credit_history_years": data.credit_history_years,
        "delinquencies": data.delinquencies
    }
    
    borrower_collection.update_one(
        {"_id": ObjectId(borrower_id)},
        {"$set": update_data}
    )
    
    return {"message": "Borrower updated"}

def delete_borrower(borrower_id):
    borrower_collection.delete_one(
        {"_id": ObjectId(borrower_id)}
    )

    return {"message": "Borrower deleted"}