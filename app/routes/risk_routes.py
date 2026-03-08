from fastapi import APIRouter
from app.services.risk_services import calculate_risk

router = APIRouter()

@router.post("/risk/assess/{borrower_id}")
def assess_risk(borrower_id: str):
    result = calculate_risk(borrower_id)
    return result