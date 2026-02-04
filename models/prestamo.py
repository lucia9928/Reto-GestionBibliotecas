from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.libro import Libro

from config.database import Base

class Prestamo(Base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    borrower_name = Column(String(100), nullable=False)
    borrower_email = Column(String(120), nullable=False)
    #FALTA VALIDAR FORMATO DE FECHA
    loan_date = Column(String, nullable=False)
    return_date = Column(String, nullable=True) #debe estar en nulo porque al crear un prestamo no se crea la fecha en que devuelve el libro
    returned = Column(Boolean, default=False)
    #foreigkey
    libro_id = Column(Integer, ForeignKey("libro.id"), nullable=False)
    # Relacion
    libro = relationship("Libro", back_populates="loans")















