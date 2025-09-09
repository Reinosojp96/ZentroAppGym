# backend/app/schemas/nutrition_schema.py
from pydantic import BaseModel
from typing import Optional, List

class Meal(BaseModel):
    name: str # e.g., "Desayuno", "Almuerzo"
    description: str
    calories: Optional[int] = None

class NutritionPlanBase(BaseModel):
    name: str
    description: Optional[str] = None
    client_id: int
    trainer_id: int
    meals: List[Meal] = []

class NutritionPlanCreate(NutritionPlanBase):
    pass

class NutritionPlanUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    meals: Optional[List[Meal]] = None

class NutritionPlan(NutritionPlanBase):
    id: int

    class Config:
        orm_mode = True
