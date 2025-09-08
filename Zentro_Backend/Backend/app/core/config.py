# core/config.py

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Clase de configuración del proyecto.
    
    Carga variables de entorno desde un archivo .env o del sistema.
    Usa Pydantic para la validación y tipado de las variables.
    """
    
    # Configuración del modelo Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",        # Carga variables desde un archivo .env
        env_file_encoding="utf-8", # Codificación del archivo
        case_sensitive=True,    # Las claves de las variables son sensibles a mayúsculas
    )

    # --- Variables de Entorno de la Aplicación ---
    
    # Clave secreta para la seguridad de la aplicación (por ejemplo, para JWT)
    # Pydantic valida que esta variable exista y no esté vacía.
    SECRET_KEY: str = Field(..., description="Clave secreta para la seguridad de la aplicación.")
    
    # Algoritmo de encriptación para los tokens JWT
    ALGORITHM: str = Field(..., description="Algoritmo de encriptación para los tokens JWT.")
    
    # Tiempo de expiración del token de acceso en minutos
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., description="Tiempo de expiración del token de acceso en minutos.")

    # --- Variables de Entorno de la Base de Datos ---
    
    # URL de conexión a la base de datos
    # Pydantic valida que esta variable exista y no esté vacía.
    DATABASE_URL: str = Field(..., description="URL de conexión a la base de datos.")
    

# Instancia de configuración que se importará en el resto del proyecto
settings = Settings()