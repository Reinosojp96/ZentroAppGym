# File: services/plan_service.py
"""
Servicio para manejar planes. Este servicio intentará usar un modelo Plan si existe
(`app.models.plan.Plan`). Si no existe, cae usando `app.models.membership.Membership`
como fallback (si el proyecto guarda planes en la tabla memberships).
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

Plan = None
FallbackMembership = None
try:
    from app.models.plan import Plan as _Plan
    Plan = _Plan
except Exception:
    try:
        from app.models.membership import Membership as _Membership
        FallbackMembership = _Membership
    except Exception:
        Plan = None
        FallbackMembership = None


class PlanService:
    def __init__(self, db: Session):
        self.db = db
        self.model = Plan or FallbackMembership

    def assert_model(self):
        if self.model is None:
            raise NotImplementedError(
                "No hay modelo Plan ni Membership detectado. Crear app.models.plan.Plan o usar app.models.membership.Membership."
            )

    def create_plan(self, **data):
        self.assert_model()
        obj = self.model(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_plan(self, plan_id: int):
        self.assert_model()
        obj = self.db.query(self.model).get(plan_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Plan not found")
        return obj

    def list_plans(self, limit: int = 100, offset: int = 0) -> List[Any]:
        self.assert_model()
        return self.db.query(self.model).offset(offset).limit(limit).all()

    def update_plan(self, plan_id: int, **updates):
        obj = self.get_plan(plan_id)
        for k, v in updates.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete_plan(self, plan_id: int):
        obj = self.get_plan(plan_id)
        self.db.delete(obj)
        self.db.commit()
        return True