from fastapi import FastAPI
from app.core.config import Settings
from app.db.base_class import Base
from app.db.session import engine
from app.api.v1 import users

settings = Settings()
app = FastAPI(title="Zentro API", version="1.0.0")
Base.metadata.create_all(bind=engine)
app.include_router(users, prefix="/api/v1/users", tags=["users"])

@app.get("/healthz")
def health():
    return {"status": "ok"}
