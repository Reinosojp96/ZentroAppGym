# backend/app/core/config.py
"""
Configuración central (Pydantic v2). Construye DATABASE_URL automáticamente
si se proporcionan DB_USER/DB_PASSWORD/DB_HOST/DB_PORT/DB_NAME.
Soporta MySQL (mysql+pymysql), PostgreSQL y SQLite.
"""
import os
from functools import lru_cache
from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Zentro SaaS"
    API_V1_STR: str = "/api/v1"

    # Opcional: URL completa. Si se provee, tiene prioridad.
    DATABASE_URL: Optional[str] = None

    # Parámetros de DB por separado (si prefieres no poner DATABASE_URL)
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[int] = None
    DB_NAME: Optional[str] = None
    DB_DRIVER: Optional[str] = None  # e.g. "pymysql" para MySQL, "asyncpg" para PG async

    # Security / JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "una_clave_secreta_muy_segura_para_desarrollo")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Network
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    BACKEND_CORS_ORIGINS: Optional[List[str]] = None

    # Pydantic v2 settings
    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        # Permitimos variables extra por si hay otras en .env que no queremos declarar.
        "extra": "allow",
    }

    def cors_origins(self) -> List[str]:
        raw = self.BACKEND_CORS_ORIGINS or os.getenv("BACKEND_CORS_ORIGINS", "")
        if not raw:
            return ["*"]
        if isinstance(raw, (list, tuple)):
            return list(raw)
        return [p.strip() for p in str(raw).split(",") if p.strip()]

    @property
    def resolved_database_url(self) -> str:
        """
        Devuelve la DATABASE_URL efectiva:
        - Si DATABASE_URL está ajustada en .env -> la usa.
        - Si no, intenta construirla a partir de DB_*.
        - Si no hay nada, fallback a sqlite local.
        """
        if self.DATABASE_URL:
            return self.DATABASE_URL

        # Necesitamos al menos DB_USER/DB_HOST/DB_NAME para construir
        if self.DB_USER and self.DB_HOST and self.DB_NAME:
            port_part = f":{self.DB_PORT}" if self.DB_PORT else ""
            # Detect driver / tipo: si DB_DRIVER contiene 'pymysql' asumimos MySQL
            # Puedes usar DB_DRIVER="pymysql" y DB_TYPE en .env si lo deseas.
            # Intentaremos detectar MySQL por DB_PORT 3306 o DB_DRIVER o DB_NAME hint.
            driver = (self.DB_DRIVER or "").lower()
            # Default: intentar MySQL si puerto 3306 o driver menciona pymysql
            if driver or (self.DB_PORT == 3306):
                # Asumir MySQL con driver pymysql
                drv = driver if driver else "pymysql"
                return f"mysql+{drv}://{self.DB_USER}:{self.DB_PASSWORD or ''}@{self.DB_HOST}{port_part}/{self.DB_NAME}"

            # De lo contrario asumimos PostgreSQL
            return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD or ''}@{self.DB_HOST}{port_part}/{self.DB_NAME}"

        # Fallback: sqlite local
        return os.getenv("DATABASE_URL", "sqlite:///./zentro.db")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
