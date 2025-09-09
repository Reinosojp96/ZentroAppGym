# backend/app/models/trainer.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    specialization = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    years_of_experience = Column(Integer, nullable=True)

    # Foreign Key para la relación uno a uno con User
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Relación bidireccional
    user = relationship("User", back_populates="trainer_details")

    # Relaciones: Un entrenador puede impartir muchas clases
    classes_taught = relationship("GymClass", back_populates="trainer")

    # Relaciones: Un entrenador puede crear muchas rutinas
    routines_created = relationship("Routine", back_populates="trainer")