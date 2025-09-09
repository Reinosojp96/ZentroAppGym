# backend/app/models/nutrition.py
"""
Define el modelo NutritionPlan, que representa un plan de dieta y nutrición
diseñado por un entrenador para un cliente.
"""
import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, DateTime, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class PlanStatus(str, enum.Enum):
    DRAFT = "Borrador"
    ACTIVE = "Activo"
    COMPLETED = "Completado"
    ARCHIVED = "Archivado"

class NutritionPlan(Base):
    __tablename__ = "nutrition_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    goal = Column(String(200), comment="Objetivo principal del plan, ej: Pérdida de peso, Aumento de masa muscular")
    status = Column(Enum(PlanStatus), default=PlanStatus.DRAFT, nullable=False, index=True)
    
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
    # Usamos JSONB para almacenar de forma eficiente la estructura del plan (comidas, alimentos, macros, etc.)
    # Esto ofrece flexibilidad y capacidad de consulta si se usa PostgreSQL.
    plan_details = Column(JSONB, nullable=False, default=lambda: {})

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    trainer_id = Column(Integer, ForeignKey("trainers.id", ondelete="SET NULL"), nullable=True)

    client = relationship("Client", back_populates="nutrition_plans")
    trainer = relationship("Trainer", back_populates="nutrition_plans")

