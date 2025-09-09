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
        from_attributes = True  # reemplaza orm_mode en Pydantic v2


# 👉 Clase que faltaba
class CheckInResponse(BaseModel):
    id: int
    client_id: int
    check_in_time: datetime.datetime

    class Config:
        from_attributes = True
