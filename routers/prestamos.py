from typing import List

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.prestamo import PrestamoResponse
from models.prestamo import Prestamo
from main import  app


@app.post("/loans",response_model=PrestamoResponse)
def registrar_prestamo():
    pass

# Listar los prestamos
@app.get("/loans", response_model=List[PrestamoResponse])
def listar_prestamos(skip: int=0, limit: int=10, db:Session=Depends(get_db)):
    prestamos = db.query(Prestamo).offset(skip).limit(limit).all()
    return  prestamos

# Listar prestamo de un libro especifico
@app.get("/loans/libro{book_id}", response_model=PrestamoResponse)
def obtener_prestamos():
    pass

@app.put("loans/{loan_id}/return")
def marcar_prestamo():
    pass