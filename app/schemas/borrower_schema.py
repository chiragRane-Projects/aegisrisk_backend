from pydantic import BaseModel

class BorrowerCreate(BaseModel):
    name: str
    age: int
    income: float
    employment_length : int
    existing_debt : float
    credit_history_years : int
    delinquencies : int