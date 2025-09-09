# backend/app/dao/membership_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Membership.
"""
from app.dao.dao_base import DaoBase
from app.models.membership import Membership
from app.schemas.membership_schema import MembershipCreate, MembershipUpdate

class membership_dao(DaoBase[Membership, MembershipCreate, MembershipUpdate]):
    def __init__(self):
        super().__init__(Membership)
