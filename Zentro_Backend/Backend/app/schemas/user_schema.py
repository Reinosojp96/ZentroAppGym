# backend/app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime

# Propiedades compartidas que todos los esquemas de usuario tendrán
class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False

# Propiedades para recibir en la creación de un usuario
class UserCreate(UserBase):
    password: str

# Propiedades para recibir en la actualización de un usuario
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_staff: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Propiedades que serán devueltas por la API
class User(UserBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
