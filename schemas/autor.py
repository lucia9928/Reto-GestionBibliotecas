from pydantic import BaseModel, EmailStr

class AutorCreate(BaseModel):
    id: int
    name: str
    nacionality: str
    birth_year:int
class AutorResponse(AutorCreate):
    class Config:
        from_attributes = True