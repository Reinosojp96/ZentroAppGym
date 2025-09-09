# backend/app/dao/trainer_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Trainer.
"""
from app.dao.dao_base import DaoBase
from app.models.trainer import Trainer
from app.schemas.trainer_schema import TrainerCreate, TrainerUpdate

class trainer_dao(DaoBase[Trainer, TrainerCreate, TrainerUpdate]):
    def __init__(self):
        super().__init__(Trainer)
