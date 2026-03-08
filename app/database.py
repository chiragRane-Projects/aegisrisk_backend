from pymongo import MongoClient
from app.config import MONGODB_URL, DATABASE_NAME

client = MongoClient(MONGODB_URL)

db = client[DATABASE_NAME]

borrower_collection = db["borrowers"]
risk_collection = db["risk_assessments"]