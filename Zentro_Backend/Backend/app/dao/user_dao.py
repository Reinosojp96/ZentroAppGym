# backend/app/dao/user_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo User.
"""
from typing import Optional
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.dao.dao_base import DaoBase
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate


class UserDao(DaoBase[User, UserCreate, UserUpdate]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
