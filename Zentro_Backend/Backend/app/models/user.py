# backend/app/models/user.py

import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class UserRole(enum.Enum):
    ADMIN = "admin"
    TRAINER = "trainer"
    CLIENT = "client"
    STAFF = "staff"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Estatus
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)

    # Rol principal del usuario en el sistema
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")

    # Relaciones: Un usuario puede ser un cliente o un entrenador
    client_details = relationship("Client", back_populates="user", uselist=False, cascade="all, delete-orphan")
    trainer_details = relationship("Trainer", back_populates="user", uselist=False, cascade="all, delete-orphan")