"""
Endpoints para la gestión de la configuración general de la aplicación.
"""
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.setting_schema import Setting, SettingUpdate # Suponiendo que existen estos esquemas
from app.services import setting_service # Suponiendo que existe este servicio

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/", response_model=Setting)
def read_settings(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene la configuración actual de la aplicación.
    """
    # Nota: Normalmente habría una única fila de configuración.
    settings = setting_service.get_settings(db)
    return settings


@router.put("/", response_model=Setting)
def update_settings(
    *,
    db: Session = Depends(get_db),
    settings_in: SettingUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza la configuración de la aplicación.
    """
    settings = setting_service.get_settings(db) # Obtener la config actual
    updated_settings = setting_service.update_settings(db=db, db_obj=settings, obj_in=settings_in)
    return updated_settings
