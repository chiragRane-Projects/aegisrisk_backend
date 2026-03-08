from fastapi import APIRouter
from app.schemas.borrower_schema import BorrowerCreate
from app.services.borrower_services import create_borrower, get_all_borrowers, get_borrower_data, update_borrower_data, delete_borrower

router = APIRouter()

@router.get("/borrowers")
def list_borrowers():
    borrowers = get_all_borrowers()

    return borrowers   

@router.get("/borrower/{borrower_id}")
def fetch_borrower(borrower_id: str):
    borrower = get_borrower_data(borrower_id)
    
    if borrower:
        return borrower
    
    return {"error": "Borrower not found"}

@router.post("/borrower")
def add_borrower(borrower: BorrowerCreate):
    result = create_borrower(borrower)
    
    return {
        "message": "Borrower created",
        "data": result
    }

@router.put("/borrower/{borrower_id}")
def modify_borrower(borrower_id: str, borrower: BorrowerCreate):
    return update_borrower_data(borrower_id, borrower)

@router.delete("/borrower/{borrower_id}")
def remove_borrower(borrower_id: str):
    return delete_borrower(borrower_id)