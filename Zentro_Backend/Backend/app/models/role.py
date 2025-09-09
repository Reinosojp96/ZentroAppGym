# backend/app/models/role.py

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# Tabla de asociación para la relación muchos a muchos entre roles y permisos
role_permissions = Table('role_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Relación: Un rol puede tener muchos usuarios
    users = relationship("User", back_populates="role")
    
    # Relación muchos a muchos con Permisos
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")