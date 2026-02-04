from fastapi import FastAPI
from config.database import Base, engine
from routers import autores, libros, prestamos
Base.metadata.create_all(bind=engine)
app = FastAPI(
title="Gestion de Bibliotecas",
description="Reto Gestion de bibliotecas",
version="1.0.0",
)
app.include_router(autores.router)
app.include_router(libros.router)
app.include_router(prestamos.router)
@app.get("/")
def read_root():
    return {"message": "gestion de Bibliotecas API"}
