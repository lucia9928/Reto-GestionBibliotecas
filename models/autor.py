from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Autor(Base):
    __tablename__ = "autor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    nacionality = Column(String(50),nullable=False)
    birth_year = Column(Integer, nullable=True)

    # Relaciones
    libros = relationship("Libro", back_populates="autores")


