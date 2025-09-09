"""
Manejo de la configuración y variables de entorno.
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings

# Es una buena práctica cargar las variables de entorno desde un archivo .env
# para facilitar el desarrollo local.
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    """
    Clase para gestionar la configuración de la aplicación utilizando Pydantic.
    Lee las variables de entorno.
    """
    PROJECT_NAME: str = "Zentro SaaS"
    API_V1_STR: str = "/api/v1"

    # Configuración de la base de datos
    # La URL de conexión se construye a partir de variables de entorno.
    # Ejemplo para PostgreSQL: postgresql://user:password@host:port/dbname
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./zentro.db")

    # Configuración de seguridad y JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "una_clave_secreta_muy_segura_para_desarrollo")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # El token expira en 30 minutos

    class Config:
        case_sensitive = True
        # Si tienes un archivo .env, Pydantic lo leerá automáticamente.
        # env_file = ".env"


# Usamos lru_cache para que la configuración se cargue una sola vez.
@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
