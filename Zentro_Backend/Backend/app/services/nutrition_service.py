# backend/app/services/nutrition_service.py
from sqlalchemy.orm import Session
from ..schemas.nutrition_schema import NutritionCreate, NutritionUpdate
from ..dao.nutrition_dao import nutrition_dao

class NutritionService:
    def get_nutrition_plan(self, db: Session, plan_id: int):
        return nutrition_dao.get(db, id=plan_id)

    def get_all_nutrition_plans(self, db: Session, skip: int = 0, limit: int = 100):
        return nutrition_dao.get_multi(db, skip=skip, limit=limit)

    def create_nutrition_plan(self, db: Session, plan_in: NutritionCreate):
        return nutrition_dao.create(db, obj_in=plan_in)

    def update_nutrition_plan(self, db: Session, plan_id: int, plan_in: NutritionUpdate):
        db_plan = self.get_nutrition_plan(db, plan_id)
        if not db_plan:
            return None
        return nutrition_dao.update(db, db_obj=db_plan, obj_in=plan_in)

    def delete_nutrition_plan(self, db: Session, plan_id: int):
        db_plan = self.get_nutrition_plan(db, plan_id)
        if not db_plan:
            return None
        return nutrition_dao.remove(db, id=plan_id)

nutrition_service = NutritionService()
