from pydantic import BaseModel
class PrestamoBase(BaseModel):
    borrower_name: str
    borrower_email: str
    loan_date: str
    return_date: str
    returned: bool
class PrestamoCreate(PrestamoBase):
    id: int
    libro_id:int
class PrestamoResponse(PrestamoBase):
    id: int
    libro_id: int
    class Config:
        from_attributes = True

