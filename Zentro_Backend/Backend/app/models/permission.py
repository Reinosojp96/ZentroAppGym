# backend/app/models/permission.py
"""
Define el modelo Permission, que representa una acción específica que un usuario puede realizar en el sistema.
Los permisos se asignan a los roles.
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

# La tabla de asociación role_permission se define aquí, pero la relación M2M
# se configura en los modelos Role y Permission.
from .role import role_permission_association

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False, comment="Nombre legible para humanos del permiso, ej: 'Crear Usuario'")
    codename = Column(String(100), unique=True, index=True, nullable=False, comment="Identificador único del permiso, ej: 'user:create'")
    description = Column(String(255), nullable=True, comment="Descripción detallada de lo que permite este permiso.")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relación muchos a muchos con Role
    roles = relationship(
        "Role",
        secondary=role_permission_association,
        back_populates="permissions"
    )

    def __repr__(self):
        return f"<Permission(name='{self.name}', codename='{self.codename}')>"

