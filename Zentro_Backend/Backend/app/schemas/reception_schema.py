# backend/app/schemas/reception_schema.py
from pydantic import BaseModel
import datetime

class CheckInBase(BaseModel):
    client_id: int

class CheckInCreate(CheckInBase):
    pass

class CheckIn(CheckInBase):
    id: int
    check_in_time: datetime.datetime

    class Config:
        orm_mode = True

