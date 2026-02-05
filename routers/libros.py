import re
from typing import List

from fastapi import HTTPException, APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.libro import libroCreate, libroResponse, libroUpdate
from models.libro import Libro


router = APIRouter(
prefix="/libros",
tags=["libros"],
)
# Crear libros
@router.post("/", response_model=libroResponse, status_code=201)
def crear_libro(libro: libroCreate,db: Session = Depends(get_db)):
    db_libro = Libro(
        title=libro.title,
        isbn=libro.isbn,
        publication_year=libro.publication_year,
        available_copies=libro.available_copies,
        autor_id=libro.autor_id
    )

    # Confirmar cambios en la base de datos
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

# Listar libros
@router.get("/", response_model=List[libroResponse])
def listar_libros(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    libros = db.query(Libro).offset(skip).limit(limit).all()
    return libros
# Buscar libro por id de libro
@router.get("/libro/{libro_id}")
def obtener_libro(libro_id: int, db: Session=Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()

    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

# Actualizar los libros

@router.put("/libro/{libro_id}/availability")
def actualizar(libro_id:int, libro_disponible:libroUpdate, db:Session=Depends(get_db)):
    db_libro= db.query(Libro).filter(Libro.id == libro_id).first()
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    db_libro.available_copies = libro_disponible.available_copies
    db.commit()
    db.refresh(db_libro)
    return db_libro




