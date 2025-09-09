# backend/app/services/trainer_service.py
from sqlalchemy.orm import Session
from ..schemas.trainer_schema import TrainerCreate, TrainerUpdate
from ..dao.trainer_dao import trainer_dao

class TrainerService:
    def get_trainer(self, db: Session, trainer_id: int):
        return trainer_dao.get(db, id=trainer_id)

    def get_all_trainers(self, db: Session, skip: int = 0, limit: int = 100):
        return trainer_dao.get_multi(db, skip=skip, limit=limit)

    def create_trainer(self, db: Session, trainer_in: TrainerCreate):
        return trainer_dao.create(db, obj_in=trainer_in)

    def update_trainer(self, db: Session, trainer_id: int, trainer_in: TrainerUpdate):
        db_trainer = self.get_trainer(db, trainer_id)
        if not db_trainer:
            return None
        return trainer_dao.update(db, db_obj=db_trainer, obj_in=trainer_in)

    def delete_trainer(self, db: Session, trainer_id: int):
        db_trainer = self.get_trainer(db, trainer_id)
        if not db_trainer:
            return None
        return trainer_dao.remove(db, id=trainer_id)

trainer_service = TrainerService()
