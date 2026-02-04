from typing import List

from fastapi import HTTPException,APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.prestamo import PrestamoResponse
from models.prestamo import Prestamo
router = APIRouter(
prefix="/prestamos",
tags=["prestamos"],
)


@router.post("/loans",response_model=PrestamoResponse)
def registrar_prestamo():
    pass

# Listar los prestamos
@router.get("/loans", response_model=List[PrestamoResponse])
def listar_prestamos(skip: int=0, limit: int=10, db:Session=Depends(get_db)):
    prestamos = db.query(Prestamo).offset(skip).limit(limit).all()
    return  prestamos

# Listar prestamo de un libro especifico
@router.get("/loans/libro{book_id}", response_model=PrestamoResponse)
def obtener_prestamos():
    prestamo = db.query(Prestamo).filter(Prestamo.libro_id == book_id).first()
    
    if not prestamo:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return prestamo

@router.put("loans/{loan_id}/return")
def marcar_prestamo():
    prestamo = db.query(Prestamo).filter(Prestamo.id == loan_id).first()
    
    if not prestamo:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    prestamo.returned = True
    db.commit()
    db.refresh(prestamo)
    return prestamo
