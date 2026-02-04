from pydantic import BaseModel, EmailStr

class AutorCreate(BaseModel):
    name: str
    nacionality: str
    birth_year:int
class AutorResponse(AutorCreate):
    id:int
    class Config:
        from_attributes = True