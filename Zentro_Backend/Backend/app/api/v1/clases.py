"""
Endpoints para la gestión de clases del gimnasio.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.class_schema import GymClass, GymClassCreate, GymClassUpdate
from app.services import class_service

router = APIRouter(prefix="/classes", tags=["classes"])


@router.post("/", response_model=GymClass, status_code=status.HTTP_201_CREATED)
def create_class(
    *,
    db: Session = Depends(get_db),
    class_in: GymClassCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea una nueva clase.
    """
    return class_service.create_class(db=db, gym_class=class_in)


@router.get("/", response_model=List[GymClass])
def read_classes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Obtiene una lista de clases.
    """
    return class_service.get_classes(db, skip=skip, limit=limit)


@router.get("/{class_id}", response_model=GymClass)
def read_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
) -> Any:
    """
    Obtiene una clase por su ID.
    """
    gym_class = class_service.get_class(db, class_id=class_id)
    if not gym_class:
        raise HTTPException(status_code=404, detail="Clase no encontrada.")
    return gym_class


@router.put("/{class_id}", response_model=GymClass)
def update_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
    class_in: GymClassUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza una clase.
    """
    gym_class = class_service.get_class(db, class_id=class_id)
    if not gym_class:
        raise HTTPException(status_code=404, detail="Clase no encontrada.")
    return class_service.update_class(db=db, db_obj=gym_class, obj_in=class_in)


@router.delete("/{class_id}", response_model=GymClass)
def delete_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina una clase.
    """
    gym_class = class_service.get_class(db, class_id=class_id)
    if not gym_class:
        raise HTTPException(status_code=404, detail="Clase no encontrada.")
    return class_service.remove_class(db=db, id=class_id)
