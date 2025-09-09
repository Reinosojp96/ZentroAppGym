# backend/app/models/reception.py
"""
Define el modelo ReceptionLog para registrar los eventos de entrada y salida
de los clientes en las instalaciones.
"""
import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class LogType(str, enum.Enum):
    CHECK_IN = "Check-in"
    CHECK_OUT = "Check-out"
    GUEST_ENTRY = "Entrada de invitado"

class ReceptionLog(Base):
    __tablename__ = "reception_logs"

    id = Column(Integer, primary_key=True, index=True)
    log_type = Column(Enum(LogType), nullable=False, default=LogType.CHECK_IN, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    notes = Column(String(500), nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, index=True)
    
    client = relationship("Client", back_populates="reception_logs")

    def __repr__(self):
        return f"<ReceptionLog(client_id={self.client_id}, type='{self.log_type}', time='{self.timestamp}')>"

