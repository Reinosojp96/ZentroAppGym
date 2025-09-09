"""
Dependencias reutilizables para los endpoints de FastAPI.
"""
from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.models import user as user_model
from app.schemas import token_schema
from app.services import user_service

# Define el esquema de autenticación. "tokenUrl" apunta al endpoint de login.
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    """
    Inyecta una sesión de base de datos en los endpoints.
    Se asegura de que la sesión se cierre siempre, incluso si hay errores.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> user_model.User:
    """
    Decodifica el token JWT para obtener el usuario actual.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = token_schema.TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No se pudieron validar las credenciales.",
        )
    user = user_service.get_user(db, user_id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


def get_current_active_user(
    current_user: user_model.User = Depends(get_current_user),
) -> user_model.User:
    """
    Verifica si el usuario actual está activo.
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Usuario inactivo.")
    return current_user
