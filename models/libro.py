from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.autor import Autor


from config.database import Base

class Libro(Base):
    __tablename__ = "libro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    publication_year = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False, default=1)

    # Relaciones
    re_autor = relationship("Autor", back_populates="libros")
    re_loans = relationship("Prestamo", back_populates="libros")

    # claves foraneas
    autor_id = Column(Integer, ForeignKey("autor.id"), nullable=False)
    prestamo_id = Column(Integer, ForeignKey("prestamo.id"), nullable=False)
