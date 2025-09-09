# backend/app/dao/routine_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Routine.
"""
from app.dao.dao_base import DaoBase
from app.models.routine import Routine
from app.schemas.routine_schema import RoutineCreate, RoutineUpdate

class RoutineDao(DaoBase[Routine, RoutineCreate, RoutineUpdate]):
    def __init__(self):
        super().__init__(Routine)
