# backend/app/schemas/client_schema.py
from pydantic import BaseModel
from typing import Optional
import datetime

class ClientBase(BaseModel):
    user_id: int
    phone_number: Optional[str] = None
    address: Optional[str] = None
    date_of_birth: Optional[datetime.date] = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    phone_number: Optional[str] = None
    address: Optional[str] = None
    date_of_birth: Optional[datetime.date] = None

class Client(ClientBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
