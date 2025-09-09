"""
Endpoints para la gestión de planes de nutrición.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.nutrition_schema import NutritionPlan, NutritionPlanCreate, NutritionPlanUpdate
from app.services import nutrition_service

router = APIRouter(prefix="/nutrition", tags=["nutrition"])


@router.post("/", response_model=NutritionPlan, status_code=status.HTTP_201_CREATED)
def create_nutrition_plan(
    *,
    db: Session = Depends(get_db),
    nutrition_in: NutritionPlanCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo plan de nutrición.
    """
    return nutrition_service.create_nutrition_plan(db=db, nutrition_plan=nutrition_in)


@router.get("/", response_model=List[NutritionPlan])
def read_nutrition_plans(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de planes de nutrición.
    """
    return nutrition_service.get_nutrition_plans(db, skip=skip, limit=limit)


@router.get("/{nutrition_id}", response_model=NutritionPlan)
def read_nutrition_plan(
    *,
    db: Session = Depends(get_db),
    nutrition_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un plan de nutrición por su ID.
    """
    plan = nutrition_service.get_nutrition_plan(db, nutrition_id=nutrition_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan de nutrición no encontrado.")
    return plan


@router.put("/{nutrition_id}", response_model=NutritionPlan)
def update_nutrition_plan(
    *,
    db: Session = Depends(get_db),
    nutrition_id: int,
    nutrition_in: NutritionPlanUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un plan de nutrición.
    """
    plan = nutrition_service.get_nutrition_plan(db, nutrition_id=nutrition_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan de nutrición no encontrado.")
    return nutrition_service.update_nutrition_plan(db=db, db_obj=plan, obj_in=nutrition_in)


@router.delete("/{nutrition_id}", response_model=NutritionPlan)
def delete_nutrition_plan(
    *,
    db: Session = Depends(get_db),
    nutrition_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un plan de nutrición.
    """
    plan = nutrition_service.get_nutrition_plan(db, nutrition_id=nutrition_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan de nutrición no encontrado.")
    return nutrition_service.remove_nutrition_plan(db=db, id=nutrition_id)
