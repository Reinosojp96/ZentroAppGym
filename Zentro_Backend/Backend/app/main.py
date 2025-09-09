# backend/app/main.py
"""
FastAPI application entrypoint para zentro_backend.

Coloca este archivo en: backend/app/main.py
Requisitos: que existan los módulos bajo app.api.v1 (cada uno exportando `router`),
app.core.config (con settings), app.db.session / app.db.init_db (opcional),
y app.core.dependencies.get_db (opcional).
"""

import logging
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
import uvicorn

# import settings / db init / dependency getter if existen
try:
    from app.core.config import settings
except Exception:
    # fallback razonable si tu config usa otros nombres:
    class _DummySettings:
        PROJECT_NAME = "zentro_backend"
        DEBUG = True
        HOST = "0.0.0.0"
        PORT = 8000
        BACKEND_CORS_ORIGINS = ["*"]

    settings = _DummySettings()

try:
    # init_db puede crear datos iniciales / tablas
    from app.db.init_db import init_db
except Exception:
    init_db = None

try:
    from app.core.dependencies import get_db
except Exception:
    get_db = None

# intentamos importar routers de app.api.v1 -- si falta alguno, lo registramos como no disponible
routers_info = [
    ("app.api.v1.users", "/users"),
    ("app.api.v1.clients", "/clients"),
    ("app.api.v1.trainers", "/trainers"),
    ("app.api.v1.memberships", "/memberships"),
    ("app.api.v1.classes", "/classes"),
    ("app.api.v1.routines", "/routines"),
    ("app.api.v1.nutrition", "/nutrition"),
    ("app.api.v1.store", "/store"),
    ("app.api.v1.incidents", "/incidents"),
    ("app.api.v1.reception", "/reception"),
    ("app.api.v1.roles", "/roles"),
    ("app.api.v1.permissions", "/permissions"),
]

_loaded_routers = []

for module_path, prefix in routers_info:
    try:
        module = __import__(module_path, fromlist=["router"])
        router = getattr(module, "router", None)
        if router is None:
            logging.warning(f"Modulo {module_path} no expone `router` — no se incluirá.")
        else:
            _loaded_routers.append((router, prefix))
    except Exception as exc:
        logging.warning(f"No se pudo importar {module_path}: {exc}")

# Aplicación
app = FastAPI(title=getattr(settings, "PROJECT_NAME", "zentro_backend"))

# CORS
origins = getattr(settings, "BACKEND_CORS_ORIGINS", None)
if origins is None:
    # soporte por compatibilidad si config usa string separado por comas
    origins = getattr(settings, "CORS_ORIGINS", ["*"])

# Asegurar formato de lista
if isinstance(origins, str):
    origins = [o.strip() for o in origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# incluir routers con prefijo /api/v1
API_PREFIX = "/api/v1"
for router, prefix in _loaded_routers:
    app.include_router(router, prefix=f"{API_PREFIX}{prefix}")

# raíz simple
@app.get("/", tags=["root"])
def read_root():
    return {
        "app": getattr(settings, "PROJECT_NAME", "zentro_backend"),
        "status": "ok",
        "api_version": "v1",
        "docs": "/docs",
    }

# Manejo de errores globales (optional pero útil)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logging.exception("Unhandled exception: %s", exc)
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Devuelve errores de validación en un formato consistente
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

# Eventos de arranque / apagado
@app.on_event("startup")
async def on_startup():
    logging.info("Starting application: %s", getattr(settings, "PROJECT_NAME", "zentro_backend"))
    # Si existe función init_db, la ejecutamos
    if init_db is not None:
        try:
            logging.info("Running database initializer (init_db)...")
            # init_db puede ser sync o async; manejamos ambos
            result = init_db()
            if hasattr(result, "__await__"):
                await result
            logging.info("Database initializer finished.")
        except Exception as e:
            logging.exception("init_db falló: %s", e)
    else:
        logging.debug("No se encontró init_db; ignorando inicialización de BD automática.")

@app.on_event("shutdown")
async def on_shutdown():
    logging.info("Shutting down application.")

# Si quieres exponer healthcheck independiente:
@app.get("/healthz", tags=["health"])
def healthz():
    return {"status": "ok"}

# Guard para ejecutar con `python -m app.main` o `python backend/app/main.py`
if __name__ == "__main__":
    host = getattr(settings, "HOST", "0.0.0.0")
    port = int(getattr(settings, "PORT", 8000))
    debug = bool(getattr(settings, "DEBUG", False))
    # uvicorn.run con reload solo conveniente en desarrollo
    uvicorn.run("app.main:app", host=host, port=port, reload=debug)
