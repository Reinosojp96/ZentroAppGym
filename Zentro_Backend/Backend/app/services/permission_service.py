# File: services/permission_service.py
"""
Servicio para permisos. CRUD básico más funciones de ayuda.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

try:
    from app.models.permission import Permission
except Exception:
    Permission = None


class PermissionService:
    def __init__(self, db: Session):
        self.db = db

    def create_permission(self, name: str, description: Optional[str] = None):
        if Permission is None:
            raise NotImplementedError("Falta el modelo app.models.permission.Permission")
        existing = self.db.query(Permission).filter(Permission.name == name).first()
        if existing:
            raise HTTPException(status_code=400, detail="Permission already exists")
        perm = Permission(name=name, description=description)
        self.db.add(perm)
        self.db.commit()
        self.db.refresh(perm)
        return perm

    def get_permission(self, permission_id: int):
        if Permission is None:
            raise NotImplementedError("Falta el modelo app.models.permission.Permission")
        perm = self.db.query(Permission).get(permission_id)
        if not perm:
            raise HTTPException(status_code=404, detail="Permission not found")
        return perm

    def list_permissions(self, limit: int = 100, offset: int = 0) -> List[Any]:
        if Permission is None:
            raise NotImplementedError("Falta el modelo app.models.permission.Permission")
        return self.db.query(Permission).offset(offset).limit(limit).all()

    def update_permission(self, permission_id: int, **updates):
        perm = self.get_permission(permission_id)
        for k, v in updates.items():
            if hasattr(perm, k):
                setattr(perm, k, v)
        self.db.add(perm)
        self.db.commit()
        self.db.refresh(perm)
        return perm

    def delete_permission(self, permission_id: int):
        perm = self.get_permission(permission_id)
        self.db.delete(perm)
        self.db.commit()
        return True
