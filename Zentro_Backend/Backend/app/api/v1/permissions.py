"""
Endpoints para la gestión de permisos.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.permission_schema import Permission
from app.services import permission_service

router = APIRouter(prefix="/permissions", tags=["permissions"])


@router.get("/", response_model=List[Permission])
def read_permissions(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de todos los permisos disponibles.
    Normalmente, los permisos son fijos en el sistema y se asignan a roles,
    por lo que no suelen tener endpoints de creación o eliminación.
    """
    permissions = permission_service.get_permissions(db, skip=skip, limit=limit)
    return permissions


@router.get("/{permission_id}", response_model=Permission)
def read_permission(
    *,
    db: Session = Depends(get_db),
    permission_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un permiso por su ID.
    """
    permission = permission_service.get_permission(db, permission_id=permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permiso no encontrado.")
    return permission

