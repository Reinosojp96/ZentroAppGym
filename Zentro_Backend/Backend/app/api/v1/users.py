from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user_schema import UserCreate, UserRead
from app.dao.user_dao import UserDAO
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    dao = UserDAO(db)
    svc = UserService(dao)
    if dao.get_by_email(user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return svc.create_user(user_in)
