# backend/app/models/client.py
"""
Define el modelo Client, que hereda de User y añade campos específicos
para los clientes del gimnasio.
"""
import enum
# Se añaden todas las importaciones necesarias, incluyendo String, Date, etc.
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base
from .user import User  # Asumimos que Client es un tipo de User

class ClientStatus(str, enum.Enum):
    ACTIVE = "Activo"
    INACTIVE = "Inactivo"
    FROZEN = "Congelado"

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    
    date_of_birth = Column(Date, nullable=True)
    phone_number = Column(String(20), nullable=True, unique=True)
    address = Column(String(255), nullable=True)
    emergency_contact_name = Column(String(100), nullable=True)
    emergency_contact_phone = Column(String(20), nullable=True)
    status = Column(Enum(ClientStatus), default=ClientStatus.ACTIVE, nullable=False, index=True)
    
    join_date = Column(Date, server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación uno a uno con User
    user = relationship("User", back_populates="client_profile")
    
    # Relaciones uno a muchos
    routines = relationship("Routine", back_populates="client", cascade="all, delete-orphan")
    nutrition_plans = relationship("NutritionPlan", back_populates="client", cascade="all, delete-orphan")
    reception_logs = relationship("ReceptionLog", back_populates="client", cascade="all, delete-orphan")
    
    # Relación con la membresía actual
    current_membership_id = Column(Integer, ForeignKey("memberships.id"), nullable=True)
    current_membership = relationship("Membership")

    def __repr__(self):
        return f"<Client(id={self.id}, user_id={self.user_id})>"
