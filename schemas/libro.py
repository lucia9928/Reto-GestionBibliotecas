from pydantic import BaseModel

class libroBase(BaseModel):
    title:str
    isbn:str
    publication_year:int
    available_copies:int
class libroCreate(libroBase):
    autor_id:int

class libroResponse(libroBase):
    id:int
    autor_id: int

    class Config:
        from_attributes = True