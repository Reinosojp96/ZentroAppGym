"""
Endpoints para la gestión de productos de la tienda.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user, get_db
from app.models.user import User as UserModel
from app.schemas.product_schema import Product, ProductCreate, ProductUpdate
from app.services import store_service

router = APIRouter(prefix="/store/products", tags=["store"])


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(
    *,
    db: Session = Depends(get_db),
    product_in: ProductCreate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Crea un nuevo producto.
    """
    return store_service.create_product(db=db, product=product_in)


@router.get("/", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Obtiene una lista de productos.
    """
    return store_service.get_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=Product)
def read_product(
    *,
    db: Session = Depends(get_db),
    product_id: int,
) -> Any:
    """
    Obtiene un producto por su ID.
    """
    product = store_service.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product


@router.put("/{product_id}", response_model=Product)
def update_product(
    *,
    db: Session = Depends(get_db),
    product_id: int,
    product_in: ProductUpdate,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Actualiza un producto.
    """
    product = store_service.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return store_service.update_product(db=db, db_obj=product, obj_in=product_in)


@router.delete("/{product_id}", response_model=Product)
def delete_product(
    *,
    db: Session = Depends(get_db),
    product_id: int,
    current_user: UserModel = Depends(get_current_active_user)
) -> Any:
    """
    Elimina un producto.
    """
    product = store_service.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return store_service.remove_product(db=db, id=product_id)
