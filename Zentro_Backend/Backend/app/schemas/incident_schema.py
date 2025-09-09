# backend/app/schemas/incident_schema.py
from pydantic import BaseModel
from typing import Optional
import datetime

class IncidentBase(BaseModel):
    reported_by_user_id: int
    title: str
    description: str
    status: str = "open" # e.g., open, in_progress, closed

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class Incident(IncidentBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
