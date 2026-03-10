from fastapi import FastAPI
from app.routes.borrower_routes import router as borrower_router
from app.routes.risk_routes import router as risk_router
from app.routes.model_routes import router as model_router

app = FastAPI()

app.include_router(borrower_router)
app.include_router(risk_router)
app.include_router(model_router)

@app.get("/")
def root():
    return {"message": "AegisRisk API is running"}