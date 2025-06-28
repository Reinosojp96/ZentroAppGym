from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base

class Plan(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
