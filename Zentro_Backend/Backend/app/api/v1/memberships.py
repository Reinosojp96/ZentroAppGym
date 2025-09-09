"""
Endpoints para la gestión de membresías.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.membership_schema import Membership, MembershipCreate, MembershipUpdate
from app.services import membership_service

router = APIRouter(prefix="/memberships", tags=["memberships"])


@router.post("/", response_model=Membership, status_code=status.HTTP_201_CREATED)
def create_membership(
    *,
    db: Session = Depends(get_db),
    membership_in: MembershipCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo tipo de membresía.
    """
    return membership_service.create_membership(db=db, membership=membership_in)


@router.get("/", response_model=List[Membership])
def read_memberships(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Obtiene una lista de membresías. No requiere autenticación.
    """
    return membership_service.get_memberships(db, skip=skip, limit=limit)


@router.get("/{membership_id}", response_model=Membership)
def read_membership(
    *,
    db: Session = Depends(get_db),
    membership_id: int,
) -> Any:
    """
    Obtiene una membresía por su ID. No requiere autenticación.
    """
    membership = membership_service.get_membership(db, membership_id=membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membresía no encontrada.")
    return membership


@router.put("/{membership_id}", response_model=Membership)
def update_membership(
    *,
    db: Session = Depends(get_db),
    membership_id: int,
    membership_in: MembershipUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza una membresía.
    """
    membership = membership_service.get_membership(db, membership_id=membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membresía no encontrada.")
    return membership_service.update_membership(db=db, db_obj=membership, obj_in=membership_in)


@router.delete("/{membership_id}", response_model=Membership)
def delete_membership(
    *,
    db: Session = Depends(get_db),
    membership_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina una membresía.
    """
    membership = membership_service.get_membership(db, membership_id=membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membresía no encontrada.")
    return membership_service.remove_membership(db=db, id=membership_id)
