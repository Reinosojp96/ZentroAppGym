# backend/app/db/database.py
"""
Configuración de la base de datos con SQLAlchemy.
Crea el engine, la sesión y el Base para los modelos.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# URL de conexión a la BD (MySQL en tu caso)
SQLALCHEMY_DATABASE_URL = settings.resolved_database_url

# Crear engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,   # Verifica conexiones antes de usarlas
    echo=False            # Cambia a True si quieres ver todas las queries en consola
)

# Crear SessionLocal (manejo de sesiones por request en FastAPI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos los modelos (los modelos deben heredar de aquí)
Base = declarative_base()

# Dependencia para inyección en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
