from fastapi import APIRouter
from app.ml.retrainer import retrain_model

router = APIRouter()

@router.post("/model/retrain")
def retrain():
    result = retrain_model()
    return {
        "message": "Model retrained successfully",
        "metadata": result
    }