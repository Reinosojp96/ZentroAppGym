# backend/app/services/user_service.py
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserCreate, UserUpdate
from ..dao.user_dao import user_dao
from ..core.security import get_password_hash

class UserService:
    def get_user(self, db: Session, user_id: int):
        return user_dao.get(db, id=user_id)

    def get_user_by_email(self, db: Session, email: str):
        return user_dao.get_by_email(db, email=email)

    def get_all_users(self, db: Session, skip: int = 0, limit: int = 100):
        return user_dao.get_multi(db, skip=skip, limit=limit)

    def create_user(self, db: Session, user_in: UserCreate):
        # Hashear la contraseña antes de guardarla
        hashed_password = get_password_hash(user_in.password)
        user_data = user_in.model_dump()
        user_data["hashed_password"] = hashed_password
        del user_data["password"]
        
        return user_dao.create(db, obj_in=user_data)

    def update_user(self, db: Session, user_id: int, user_in: UserUpdate):
        db_user = self.get_user(db, user_id)
        if not db_user:
            return None
        
        update_data = user_in.model_dump(exclude_unset=True)
        
        if "password" in update_data and update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            update_data["hashed_password"] = hashed_password
            del update_data["password"]
            
        return user_dao.update(db, db_obj=db_user, obj_in=update_data)

    def delete_user(self, db: Session, user_id: int):
        db_user = self.get_user(db, user_id)
        if not db_user:
            return None
        return user_dao.remove(db, id=user_id)

user_service = UserService()
