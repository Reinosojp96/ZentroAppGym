"""
Endpoints para la gestión de recepción (check-in/check-out).
"""
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.reception_schema import CheckInCreate, CheckInResponse
from app.services import reception_service

router = APIRouter(prefix="/reception", tags=["reception"])


@router.post("/check-in", response_model=CheckInResponse, status_code=status.HTTP_201_CREATED)
def client_check_in(
    *,
    db: Session = Depends(get_db),
    check_in_data: CheckInCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Realiza el check-in de un cliente.
    Valida la membresía y registra la entrada.
    """
    response = reception_service.check_in(db=db, check_in_info=check_in_data)
    if not response["status"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

# Aquí se podrían añadir más endpoints en el futuro, como:
# - Check-out de clientes
# - Verificación de estado de membresía por ID
# - Registro de visitas de invitados

