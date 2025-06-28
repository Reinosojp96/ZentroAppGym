from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class GymClass(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    instructor = Column(String(100))
    schedule = Column(String(100))
