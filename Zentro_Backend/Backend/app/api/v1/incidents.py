"""
Endpoints para la gestión de incidentes.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.incident_schema import Incident, IncidentCreate, IncidentUpdate
from app.services import incident_service

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("/", response_model=Incident, status_code=status.HTTP_201_CREATED)
def create_incident(
    *,
    db: Session = Depends(get_db),
    incident_in: IncidentCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo incidente.
    """
    return incident_service.create_incident(db=db, incident=incident_in)


@router.get("/", response_model=List[Incident])
def read_incidents(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de incidentes.
    """
    return incident_service.get_incidents(db, skip=skip, limit=limit)


@router.get("/{incident_id}", response_model=Incident)
def read_incident(
    *,
    db: Session = Depends(get_db),
    incident_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un incidente por su ID.
    """
    incident = incident_service.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado.")
    return incident


@router.put("/{incident_id}", response_model=Incident)
def update_incident(
    *,
    db: Session = Depends(get_db),
    incident_id: int,
    incident_in: IncidentUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un incidente.
    """
    incident = incident_service.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado.")
    return incident_service.update_incident(db=db, db_obj=incident, obj_in=incident_in)


@router.delete("/{incident_id}", response_model=Incident)
def delete_incident(
    *,
    db: Session = Depends(get_db),
    incident_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un incidente.
    """
    incident = incident_service.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado.")
    return incident_service.remove_incident(db=db, id=incident_id)
