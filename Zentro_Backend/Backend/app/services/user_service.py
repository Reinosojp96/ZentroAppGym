from app.dao.user_dao import UserDAO
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash, verify_password
from app.models.user import User

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_user(self, data: UserCreate):
        hashed = get_password_hash(data.password)
        user = User(email=data.email, hashed_password=hashed)
        return self.dao.create(user)
