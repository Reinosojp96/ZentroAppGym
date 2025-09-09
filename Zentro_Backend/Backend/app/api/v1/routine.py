"""
Endpoints para la gestión de rutinas de ejercicio.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.routine_schema import Routine, RoutineCreate, RoutineUpdate
from app.services import routine_service

router = APIRouter(prefix="/routines", tags=["routines"])


@router.post("/", response_model=Routine, status_code=status.HTTP_201_CREATED)
def create_routine(
    *,
    db: Session = Depends(get_db),
    routine_in: RoutineCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea una nueva rutina.
    """
    return routine_service.create_routine(db=db, routine=routine_in)


@router.get("/", response_model=List[Routine])
def read_routines(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de rutinas.
    """
    return routine_service.get_routines(db, skip=skip, limit=limit)


@router.get("/{routine_id}", response_model=Routine)
def read_routine(
    *,
    db: Session = Depends(get_db),
    routine_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene una rutina por su ID.
    """
    routine = routine_service.get_routine(db, routine_id=routine_id)
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina no encontrada.")
    return routine


@router.put("/{routine_id}", response_model=Routine)
def update_routine(
    *,
    db: Session = Depends(get_db),
    routine_id: int,
    routine_in: RoutineUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza una rutina.
    """
    routine = routine_service.get_routine(db, routine_id=routine_id)
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina no encontrada.")
    return routine_service.update_routine(db=db, db_obj=routine, obj_in=routine_in)


@router.delete("/{routine_id}", response_model=Routine)
def delete_routine(
    *,
    db: Session = Depends(get_db),
    routine_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina una rutina.
    """
    routine = routine_service.get_routine(db, routine_id=routine_id)
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina no encontrada.")
    return routine_service.remove_routine(db=db, id=routine_id)
