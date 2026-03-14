from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.borrower_routes import router as borrower_router
from app.routes.risk_routes import router as risk_router
from app.routes.model_routes import router as model_router
from app.routes.analytics_routes import router as analytics_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(borrower_router)
app.include_router(risk_router)
app.include_router(model_router)
app.include_router(analytics_router)

@app.get("/")
def root():
    return {"message": "AegisRisk API is running"}