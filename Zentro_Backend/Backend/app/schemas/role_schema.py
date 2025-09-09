# backend/app/schemas/role_schema.py
from pydantic import BaseModel
from typing import Optional, List

# Adelantamos la declaración para usarla en Role
class Permission(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Role(RoleBase):
    id: int
    permissions: List[Permission] = []

    class Config:
        from_attributes = True

