"""
Endpoints para la gestión de clientes.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.client_schema import Client, ClientCreate, ClientUpdate
from app.services import client_service

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def create_client(
    *,
    db: Session = Depends(get_db),
    client_in: ClientCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo cliente.
    """
    return client_service.create_client(db=db, client=client_in)


@router.get("/", response_model=List[Client])
def read_clients(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> Any:
    """
    Obtiene una lista de clientes.
    """
    return client_service.get_clients(db, skip=skip, limit=limit)


@router.get("/{client_id}", response_model=Client)
def read_client(
    *,
    db: Session = Depends(get_db),
    client_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Obtiene un cliente por su ID.
    """
    client = client_service.get_client(db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return client


@router.put("/{client_id}", response_model=Client)
def update_client(
    *,
    db: Session = Depends(get_db),
    client_id: int,
    client_in: ClientUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un cliente.
    """
    client = client_service.get_client(db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return client_service.update_client(db=db, db_obj=client, obj_in=client_in)


@router.delete("/{client_id}", response_model=Client)
def delete_client(
    *,
    db: Session = Depends(get_db),
    client_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un cliente.
    """
    client = client_service.get_client(db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return client_service.remove_client(db=db, id=client_id)
