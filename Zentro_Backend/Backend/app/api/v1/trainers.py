"""
Endpoints para la gestión de entrenadores.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.trainer_schema import Trainer, TrainerCreate, TrainerUpdate
from app.services import trainer_service

router = APIRouter(prefix="/trainers", tags=["trainers"])


@router.post("/", response_model=Trainer, status_code=status.HTTP_201_CREATED)
def create_trainer(
    *,
    db: Session = Depends(get_db),
    trainer_in: TrainerCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo entrenador.
    """
    return trainer_service.create_trainer(db=db, trainer=trainer_in)


@router.get("/", response_model=List[Trainer])
def read_trainers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de entrenadores.
    """
    return trainer_service.get_trainers(db, skip=skip, limit=limit)


@router.get("/{trainer_id}", response_model=Trainer)
def read_trainer(
    *,
    db: Session = Depends(get_db),
    trainer_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un entrenador por su ID.
    """
    trainer = trainer_service.get_trainer(db, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Entrenador no encontrado.")
    return trainer


@router.put("/{trainer_id}", response_model=Trainer)
def update_trainer(
    *,
    db: Session = Depends(get_db),
    trainer_id: int,
    trainer_in: TrainerUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un entrenador.
    """
    trainer = trainer_service.get_trainer(db, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Entrenador no encontrado.")
    return trainer_service.update_trainer(db=db, db_obj=trainer, obj_in=trainer_in)


@router.delete("/{trainer_id}", response_model=Trainer)
def delete_trainer(
    *,
    db: Session = Depends(get_db),
    trainer_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un entrenador.
    """
    trainer = trainer_service.get_trainer(db, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Entrenador no encontrado.")
    return trainer_service.remove_trainer(db=db, id=trainer_id)
