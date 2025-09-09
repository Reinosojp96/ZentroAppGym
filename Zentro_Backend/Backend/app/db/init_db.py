# backend/app/db/init_db.py
"""
Script o función para inicializar la base de datos con datos primarios.
Por ejemplo, crear el primer superusuario.
"""
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.user_schema import UserCreate
from app.services import user_service

def init_db(db: Session) -> None:
    """
    Inicializa la base de datos.
    """
    # Esta función se podría llamar al iniciar la aplicación en un entorno de desarrollo.
    # Crea el primer superusuario si no existe, usando los datos de config.py.
    user = user_service.get_user_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name="Admin" # Puedes añadir más campos por defecto si quieres
        )
        user = user_service.create_user(db, user=user_in)
        print(f"Superuser '{settings.FIRST_SUPERUSER}' created.")
    else:
        print(f"Superuser '{settings.FIRST_SUPERUSER}' already exists.")