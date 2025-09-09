# backend/app/schemas/nutrition_schema.py
from pydantic import BaseModel
from typing import Optional, List

class Meal(BaseModel):
    name: str # e.g., "Desayuno", "Almuerzo"
    description: str
    calories: Optional[int] = None

class NutritionBase(BaseModel):
    name: str
    description: Optional[str] = None
    client_id: int
    trainer_id: int
    meals: List[Meal] = []

class NutritionCreate(NutritionBase):
    pass

class NutritionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    meals: Optional[List[Meal]] = None

class Nutrition(NutritionBase):
    id: int

    class Config:
        from_attributes = True
