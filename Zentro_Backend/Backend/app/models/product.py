# backend/app/models/product.py
"""
Define el modelo Product para los artículos vendidos en la tienda del gimnasio
(suplementos, ropa, bebidas, etc.).
"""
from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True, nullable=False)
    sku = Column(String(50), unique=True, index=True, nullable=False, comment="Stock Keeping Unit")
    description = Column(Text, nullable=True)
    
    # Usar Numeric para precios para evitar problemas de punto flotante.
    # precision=10, scale=2 significa hasta 10 dígitos en total, con 2 decimales.
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, default=0, nullable=False)
    
    is_active = Column(Boolean, default=True, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Se podría agregar una relación a una tabla de categorías de productos
    # category_id = Column(Integer, ForeignKey("product_categories.id"))
    # category = relationship("ProductCategory", back_populates="products")

    def __repr__(self):
        return f"<Product(name='{self.name}', sku='{self.sku}')>"

