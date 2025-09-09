# backend/app/services/membership_service.py
from sqlalchemy.orm import Session
from ..schemas.membership_schema import MembershipCreate, MembershipUpdate
from ..dao.membership_dao import membership_dao

class MembershipService:
    def get_membership(self, db: Session, membership_id: int):
        return membership_dao.get(db, id=membership_id)

    def get_all_memberships(self, db: Session, skip: int = 0, limit: int = 100):
        return membership_dao.get_multi(db, skip=skip, limit=limit)

    def create_membership(self, db: Session, membership_in: MembershipCreate):
        return membership_dao.create(db, obj_in=membership_in)

    def update_membership(self, db: Session, membership_id: int, membership_in: MembershipUpdate):
        db_membership = self.get_membership(db, membership_id)
        if not db_membership:
            return None
        return membership_dao.update(db, db_obj=db_membership, obj_in=membership_in)

    def delete_membership(self, db: Session, membership_id: int):
        db_membership = self.get_membership(db, membership_id)
        if not db_membership:
            return None
        return membership_dao.remove(db, id=membership_id)

membership_service = MembershipService()
