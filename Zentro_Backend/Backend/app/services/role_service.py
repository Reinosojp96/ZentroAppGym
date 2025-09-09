# File: services/role_service.py
"""
Servicio para roles: CRUD y asignación de permisos.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

try:
    from app.models.role import Role
    from app.models.permission import Permission
except Exception:
    Role = None
    Permission = None


class RoleService:
    def __init__(self, db: Session):
        self.db = db

    def create_role(self, name: str, description: Optional[str] = None):
        if Role is None:
            raise NotImplementedError("Falta el modelo app.models.role.Role")
        existing = self.db.query(Role).filter(Role.name == name).first()
        if existing:
            raise HTTPException(status_code=400, detail="Role already exists")
        role = Role(name=name, description=description)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def get_role(self, role_id: int):
        if Role is None:
            raise NotImplementedError("Falta el modelo app.models.role.Role")
        role = self.db.query(Role).get(role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    def list_roles(self, limit: int = 100, offset: int = 0) -> List[Any]:
        if Role is None:
            raise NotImplementedError("Falta el modelo app.models.role.Role")
        return self.db.query(Role).offset(offset).limit(limit).all()

    def update_role(self, role_id: int, **updates):
        role = self.get_role(role_id)
        for k, v in updates.items():
            if hasattr(role, k):
                setattr(role, k, v)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete_role(self, role_id: int):
        role = self.get_role(role_id)
        self.db.delete(role)
        self.db.commit()
        return True

    def assign_permissions(self, role_id: int, permission_ids: List[int]):
        """Asigna permisos existentes al rol. Asume relación many-to-many `role.permissions`."""
        role = self.get_role(role_id)
        if Permission is None:
            raise NotImplementedError("Falta app.models.permission.Permission")
        perms = self.db.query(Permission).filter(Permission.id.in_(permission_ids)).all()
        if len(perms) != len(permission_ids):
            found_ids = {p.id for p in perms}
            missing = set(permission_ids) - found_ids
            raise HTTPException(status_code=404, detail=f"Permissions not found: {missing}")
        # Asignación --- depende de la relación declarada en el modelo
        if not hasattr(role, 'permissions'):
            raise NotImplementedError("El modelo Role no tiene atributo 'permissions' para relación ManyToMany")
        role.permissions = perms
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role