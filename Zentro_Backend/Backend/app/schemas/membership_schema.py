# backend/app/schemas/membership_schema.py
from pydantic import BaseModel
from typing import Optional
import datetime

class MembershipBase(BaseModel):
    client_id: int
    membership_type: str
    start_date: datetime.date
    end_date: datetime.date
    status: str = "active" # por ejemplo: active, expired, frozen

class MembershipCreate(MembershipBase):
    pass

class MembershipUpdate(BaseModel):
    membership_type: Optional[str] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    status: Optional[str] = None

class Membership(MembershipBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
