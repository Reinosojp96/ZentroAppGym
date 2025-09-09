# backend/app/schemas/class_schema.py
from pydantic import BaseModel
from typing import Optional, List
import datetime

class GymClassBase(BaseModel):
    name: str
    description: Optional[str] = None
    trainer_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    max_capacity: int

class GymClassCreate(GymClassBase):
    pass

class GymClassUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    trainer_id: Optional[int] = None
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None
    max_capacity: Optional[int] = None

class GymClass(GymClassBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
