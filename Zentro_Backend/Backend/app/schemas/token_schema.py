# app/schemas/token_schema.py
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str | None = None  # user id o username
    exp: int | None = None  # expiry timestamp
