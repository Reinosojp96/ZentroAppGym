"""
Endpoints para la gestión de roles de usuario.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.role_schema import Role, RoleCreate, RoleUpdate
from app.services import role_service

router = APIRouter(prefix="/roles", tags=["roles"])


@router.post("/", response_model=Role, status_code=status.HTTP_201_CREATED)
def create_role(
    *,
    db: Session = Depends(get_db),
    role_in: RoleCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo rol.
    """
    return role_service.create_role(db=db, role=role_in)


@router.get("/", response_model=List[Role])
def read_roles(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de roles.
    """
    return role_service.get_roles(db, skip=skip, limit=limit)


@router.get("/{role_id}", response_model=Role)
def read_role(
    *,
    db: Session = Depends(get_db),
    role_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un rol por su ID.
    """
    role = role_service.get_role(db, role_id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")
    return role


@router.put("/{role_id}", response_model=Role)
def update_role(
    *,
    db: Session = Depends(get_db),
    role_id: int,
    role_in: RoleUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un rol. Se pueden asignar permisos a un rol.
    """
    role = role_service.get_role(db, role_id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")
    return role_service.update_role(db=db, db_obj=role, obj_in=role_in)


@router.delete("/{role_id}", response_model=Role)
def delete_role(
    *,
    db: Session = Depends(get_db),
    role_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un rol.
    """
    role = role_service.get_role(db, role_id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")
    return role_service.remove_role(db=db, id=role_id)

