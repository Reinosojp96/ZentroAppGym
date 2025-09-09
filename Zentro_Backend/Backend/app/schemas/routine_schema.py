# backend/app/schemas/routine_schema.py
from pydantic import BaseModel
from typing import Optional, List

class Exercise(BaseModel):
    name: str
    sets: int
    reps: str # Puede ser un rango como "8-12"
    rest_period: Optional[str] = "60s"

class RoutineBase(BaseModel):
    name: str
    description: Optional[str] = None
    client_id: int
    trainer_id: int
    exercises: List[Exercise] = []

class RoutineCreate(RoutineBase):
    pass

class RoutineUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    exercises: Optional[List[Exercise]] = None

class Routine(RoutineBase):
    id: int

    class Config:
        orm_mode = True
