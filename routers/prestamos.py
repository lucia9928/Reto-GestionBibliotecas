from typing import List
from datetime import date
from fastapi import HTTPException,APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.prestamo import PrestamoResponse, PrestamoCreate
from models.prestamo import Prestamo
from models.libro  import Libro

router = APIRouter(
prefix="/prestamos",
tags=["prestamos"],
)


@router.post("/loans",response_model=PrestamoResponse)
def registrar_prestamo(prestamo:PrestamoCreate, db:Session=Depends(get_db)):
    # Verificar que el libro exista
    libro = db.query(Libro).filter(Libro.id == prestamo.libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="libro no encontrado")
    if libro.available_copies < 1:
        raise HTTPException(status_code=400, detail="No hay copias disponibles")

    db_prestamo = Prestamo(
        libro_id=prestamo.libro_id,
        borrower_name=prestamo.borrower_name,
        borrower_email=prestamo.borrower_email,
        loan_date=date.today().isoformat(),
        return_date=None,
        returned= False

    )
    libro.available_copies -=1

    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo


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
