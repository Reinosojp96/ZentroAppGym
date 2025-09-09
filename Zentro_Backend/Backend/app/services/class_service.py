# backend/app/services/class_service.py
from sqlalchemy.orm import Session
from ..schemas.class_schema import ClassCreate, ClassUpdate
from ..dao.class_dao import gym_class_dao

class ClassService:
    def get_class(self, db: Session, class_id: int):
        return gym_class_dao.get(db, id=class_id)

    def get_all_classes(self, db: Session, skip: int = 0, limit: int = 100):
        return gym_class_dao.get_multi(db, skip=skip, limit=limit)

    def create_class(self, db: Session, class_in: ClassCreate):
        return gym_class_dao.create(db, obj_in=class_in)

    def update_class(self, db: Session, class_id: int, class_in: ClassUpdate):
        db_class = self.get_class(db, class_id)
        if not db_class:
            return None
        return gym_class_dao.update(db, db_obj=db_class, obj_in=class_in)

    def delete_class(self, db: Session, class_id: int):
        db_class = self.get_class(db, class_id)
        if not db_class:
            return None
        return gym_class_dao.remove(db, id=class_id)

class_service = ClassService()
