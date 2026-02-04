from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.libro import Libro

from config.database import Base

class Prestamo(Base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey=Libro.id)
    borrower_name = Column(String(100), nullable=False)
    borrower_email = Column(String(120), nullable=False)
    #FALTA VALIDAR FORMATO DE FECHA
    loan_date = Column(String, nullable=False)
    return_date = Column(String, nullable=False)

    # Relacion
    re_libro = relationship("Libro", back_populates="prestamos")















