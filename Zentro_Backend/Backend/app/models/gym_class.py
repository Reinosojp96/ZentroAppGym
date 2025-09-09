# backend/app/models/gym_class.py

from sqlalchemy import Column, Integer, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class GymClass(Base):
    __tablename__ = "gym_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    capacity = Column(Integer, nullable=False)

    # Foreign Key
    trainer_id = Column(Integer, ForeignKey("trainers.id"), nullable=False)

    # Relaciones
    trainer = relationship("Trainer", back_populates="classes_taught")
    
    # (Opcional) Relación para reservas de clientes
    # bookings = relationship("ClassBooking", back_populates="gym_class")