# backend/app/dao/nutrition_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Nutrition.
"""
from app.dao.dao_base import DaoBase
from app.models.nutrition import Nutrition
from app.schemas.nutrition_schema import NutritionCreate, NutritionUpdate

class nutrition_dao(DaoBase[Nutrition, NutritionCreate, NutritionUpdate]):
    def __init__(self):
        super().__init__(Nutrition)
