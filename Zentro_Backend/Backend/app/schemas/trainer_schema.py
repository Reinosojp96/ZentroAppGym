# backend/app/schemas/trainer_schema.py
from pydantic import BaseModel
from typing import Optional, List
import datetime

class TrainerBase(BaseModel):
    user_id: int
    specialization: Optional[str] = None
    bio: Optional[str] = None
    years_of_experience: Optional[int] = 0

class TrainerCreate(TrainerBase):
    pass

class TrainerUpdate(BaseModel):
    specialization: Optional[str] = None
    bio: Optional[str] = None
    years_of_experience: Optional[int] = None

class Trainer(TrainerBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
