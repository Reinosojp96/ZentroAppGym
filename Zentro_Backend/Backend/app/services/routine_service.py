# backend/app/services/routine_service.py
from sqlalchemy.orm import Session
from ..schemas.routine_schema import RoutineCreate, RoutineUpdate
from ..dao.routine_dao import routine_dao

class RoutineService:
    def get_routine(self, db: Session, routine_id: int):
        return routine_dao.get(db, id=routine_id)

    def get_all_routines(self, db: Session, skip: int = 0, limit: int = 100):
        return routine_dao.get_multi(db, skip=skip, limit=limit)

    def create_routine(self, db: Session, routine_in: RoutineCreate):
        return routine_dao.create(db, obj_in=routine_in)

    def update_routine(self, db: Session, routine_id: int, routine_in: RoutineUpdate):
        db_routine = self.get_routine(db, routine_id)
        if not db_routine:
            return None
        return routine_dao.update(db, db_obj=db_routine, obj_in=routine_in)

    def delete_routine(self, db: Session, routine_id: int):
        db_routine = self.get_routine(db, routine_id)
        if not db_routine:
            return None
        return routine_dao.remove(db, id=routine_id)

routine_service = RoutineService()
