# backend/app/models/incident.py
"""
Define el modelo Incident para el seguimiento de problemas, fallos de equipo o cualquier
otro incidente que requiera atención y resolución.
"""
import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class IncidentStatus(str, enum.Enum):
    OPEN = "Abierto"
    IN_PROGRESS = "En Progreso"
    RESOLVED = "Resuelto"
    CLOSED = "Cerrado"

class IncidentPriority(str, enum.Enum):
    LOW = "Baja"
    MEDIUM = "Media"
    HIGH = "Alta"
    CRITICAL = "Crítica"

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.OPEN, nullable=False, index=True)
    priority = Column(Enum(IncidentPriority), default=IncidentPriority.MEDIUM, nullable=False, index=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)

    reported_by_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    assigned_to_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    reported_by = relationship("User", foreign_keys=[reported_by_id], back_populates="reported_incidents")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id], back_populates="assigned_incidents")

    def __repr__(self):
        return f"<Incident(title='{self.title}', status='{self.status}')>"

