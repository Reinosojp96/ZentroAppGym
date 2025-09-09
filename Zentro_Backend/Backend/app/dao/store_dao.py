# backend/app/dao/store_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Product.
"""
from app.dao.dao_base import DaoBase
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate

class product_dao(DaoBase[Product, ProductCreate, ProductUpdate]):
    def __init__(self):
        super().__init__(Product)
