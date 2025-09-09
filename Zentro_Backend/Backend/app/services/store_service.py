# backend/app/services/store_service.py
from sqlalchemy.orm import Session
from ..schemas.product_schema import ProductCreate, ProductUpdate
from ..dao.store_dao import product_dao

class StoreService:
    def get_product(self, db: Session, product_id: int):
        return product_dao.get(db, id=product_id)

    def get_all_products(self, db: Session, skip: int = 0, limit: int = 100):
        return product_dao.get_multi(db, skip=skip, limit=limit)

    def create_product(self, db: Session, product_in: ProductCreate):
        return product_dao.create(db, obj_in=product_in)

    def update_product(self, db: Session, product_id: int, product_in: ProductUpdate):
        db_product = self.get_product(db, product_id)
        if not db_product:
            return None
        return product_dao.update(db, db_obj=db_product, obj_in=product_in)

    def delete_product(self, db: Session, product_id: int):
        db_product = self.get_product(db, product_id)
        if not db_product:
            return None
        return product_dao.remove(db, id=product_id)

store_service = StoreService()
