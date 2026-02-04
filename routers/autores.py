from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.autor import Autor
from schemas.autor import AutorCreate, AutorResponse
router = APIRouter(
prefix="/autores",
tags=["autores"],
)

@router.post("/", response_model=AutorResponse)
def create_autor(autor: AutorCreate, db: Session = Depends(get_db)):
    db_autor = Autor(name=autor.name, nacionality=autor.nacionality, birth_year=autor.birth_year)
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

@router.get("/", response_model=List[AutorResponse])
def list_autores(db: Session = Depends(get_db)):
    autores = db.query(Autor).all()
    return autores

@router.get("/{autor_id}", response_model=AutorResponse)
def get_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if not autor:
         raise HTTPException(status_code=404, detail="autor not found")
    return autor