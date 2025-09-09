# backend/app/models/routine.py
"""
Define el modelo Routine, que representa un plan de entrenamiento (rutina)
creado por un entrenador para un cliente.
"""
import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class DifficultyLevel(str, enum.Enum):
    BEGINNER = "Principiante"
    INTERMEDIATE = "Intermedio"
    ADVANCED = "Avanzado"

class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    focus = Column(String(200), comment="Enfoque de la rutina, ej: Hipertrofia, Fuerza, Resistencia")
    difficulty = Column(Enum(DifficultyLevel), default=DifficultyLevel.INTERMEDIATE, nullable=False)

    # Usamos JSONB para una estructura flexible de ejercicios, series, repeticiones, etc.
    exercises_plan = Column(JSONB, nullable=False, default=lambda: {})

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    trainer_id = Column(Integer, ForeignKey("trainers.id", ondelete="SET NULL"), nullable=True)

    client = relationship("Client", back_populates="routines")
    trainer = relationship("Trainer", back_populates="routines")

