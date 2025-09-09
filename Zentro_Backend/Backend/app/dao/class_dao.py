# backend/app/dao/class_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo GymClass.
"""
from app.dao.dao_base import DaoBase
from app.models.gym_class import GymClass
from app.schemas.class_schema import ClassCreate, ClassUpdate

class gym_class_dao(DaoBase[GymClass, ClassCreate, ClassUpdate]):
    def __init__(self):
        super().__init__(GymClass)
