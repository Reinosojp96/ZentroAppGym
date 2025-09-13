# backend/app/api/v1/auth.py
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session


from app.core.dependencies import get_db
from app.models.user import User


try:
    from app.core.config import settings
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = settings.ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
except Exception:
    # valores por defecto (cámbialos en producción)
    SECRET_KEY = "replace-with-a-secure-random-string"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 días por defecto

router = APIRouter(tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


# -----------------------
# Schemas
# -----------------------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_at: Optional[datetime] = None


class TokenData(BaseModel):
    sub: Optional[str] = None  # usually user id or email


class UserCreate(BaseModel):
    id: int  # número de documento, ahora clave primaria
    document_type: str  # "C.C", "T.I", "Pasaporte", "Otro"
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: str



class UserOut(BaseModel):
    id: int
    document_type: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        from_attributes = True



# -----------------------
# Helpers
# -----------------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt, expire


# -----------------------
# DB helpers (simple/standard SQLAlchemy)
# -----------------------
def get_user_by_email(db: Session, email: str):
    """Ajusta esta función si tu modelo de usuario o campo email es distinto."""
    return db.query(User).filter(User.email == email).first()


def create_user_in_db(db: Session, user_in: UserCreate):
    hashed = get_password_hash(user_in.password)
    user = User(
        id=user_in.id,  # documento como clave primaria
        document_type=user_in.document_type,
        email=user_in.email,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        hashed_password=hashed,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    # asumo que tu modelo User tiene `hashed_password`
    if not verify_password(password, getattr(user, "hashed_password", "")):
        return None
    return user


# -----------------------
# Endpoints
# -----------------------

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario.
    Devuelve el usuario (sin password).
    """
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    user = create_user_in_db(db, user_in)
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Endpoint estándar OAuth2 compatible con `OAuth2PasswordRequestForm`.
    Nota: form_data.username puede ser email o username según tu implementación.
    """
    email = form_data.username
    password = form_data.password
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales inválidas",
                            headers={"WWW-Authenticate": "Bearer"})
    token_payload = {"sub": str(user.id)}
    token, expire = create_access_token(token_payload)
    return {"access_token": token, "token_type": "bearer", "expires_at": expire}


# Alternativa: login que acepta JSON { "email": "...", "password":"..." }
class LoginIn(BaseModel):
    email: EmailStr
    password: str


@router.post("/login", response_model=Token)
def login_json(credentials: LoginIn, db: Session = Depends(get_db)):
    user = authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales inválidas")
    token_payload = {"sub": str(user.id)}
    token, expire = create_access_token(token_payload)
    return {"access_token": token, "token_type": "bearer", "expires_at": expire}


# -----------------------
# Dependency para obtener usuario actual
# -----------------------
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub = payload.get("sub")
        if sub is None:
            raise credentials_exception
        token_data = TokenData(sub=sub)
    except JWTError:
        raise credentials_exception

    user = db.query(User).get(int(token_data.sub))
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user=Depends(get_current_user)):
    # Si tu modelo tiene flag is_active u otro, valida aquí
    if getattr(current_user, "is_active", True) is False:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user


@router.get("/me", response_model=UserOut)
def read_users_me(current_user=Depends(get_current_active_user)):
    return current_user
