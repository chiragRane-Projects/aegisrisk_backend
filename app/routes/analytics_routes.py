from fastapi import APIRouter
from app.services.analytics_service import portfolio_summary, risk_distribution, high_risk_borrowers

router = APIRouter()

@router.get("/analytics/portfolio-summary")
def portfolio():
    return portfolio_summary()

@router.get("/analytics/risk-distribution")
def distribution():
    return risk_distribution()

@router.get("/analytics/high-risk-borrowers")
def risky():
    return high_risk_borrowers()