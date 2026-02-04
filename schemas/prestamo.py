from pydantic import BaseModel, EmailStr, field_validator
import re
from typing import Optional

DATE_REGEX = r"^\d{4}-\d{2}-\d{2}$"
class PrestamoBase(BaseModel):
    borrower_name: str
    borrower_email: EmailStr #validacion para el email

class PrestamoCreate(PrestamoBase):
    libro_id:int
class PrestamoResponse(PrestamoBase):
    id: int
    libro_id: int
    loan_date: str
    return_date: Optional[str]
    returned: bool

    # validacion de la fecha usamos un string al que llama
    @field_validator('loan_date', 'return_date', mode='before')
    def check_date_format(cls, v):
        if v is None:
            return v
        if not re.match(DATE_REGEX, v):
            raise ValueError('Fecha debe tener formato YYYY-MM-DD')
        return v
    class Config:
        from_attributes = True

