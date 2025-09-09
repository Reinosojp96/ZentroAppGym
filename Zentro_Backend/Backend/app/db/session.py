# backend/app/db/session.py
"""
Configuración de la conexión a la base de datos con SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Crea el motor de la base de datos.
# 'connect_args' es necesario solo para SQLite para permitir el uso en múltiples hilos (como lo hace FastAPI).
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Crea una fábrica de sesiones. Esta será la que usemos para crear nuevas sesiones de BD.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

