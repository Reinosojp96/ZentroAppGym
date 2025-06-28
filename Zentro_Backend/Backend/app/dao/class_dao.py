from sqlalchemy.orm import Session
from app.models.gym_class import GymClass

class ClassDAO:
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return self.db.query(GymClass).all()
