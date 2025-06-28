from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from app.db.base_class import Base
import datetime

class Payment(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
