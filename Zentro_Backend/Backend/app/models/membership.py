# backend/app/models/membership.py
"""
Define el modelo Membership para los planes y tipos de membresía que ofrece el gimnasio.
"""
import enum
# Se añaden todas las importaciones necesarias
from sqlalchemy import Column, Integer, String, Numeric, Enum, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class MembershipDurationType(str, enum.Enum):
    DAY = "Día(s)"
    WEEK = "Semana(s)"
    MONTH = "Mes(es)"
    YEAR = "Año(s)"

class Membership(Base):
    __tablename__ = "memberships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    
    # Usamos Numeric para la precisión monetaria
    price = Column(Numeric(10, 2), nullable=False)
    
    duration_value = Column(Integer, nullable=False, comment="Ej: 1, 3, 6, 12")
    duration_type = Column(Enum(MembershipDurationType), nullable=False, default=MembershipDurationType.MONTH)
    
    is_active = Column(Boolean, default=True, nullable=False, comment="Indica si esta membresía se puede seguir vendiendo")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Membership(name='{self.name}', price={self.price})>"
