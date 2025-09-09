# backend/app/models/payment.py

from sqlalchemy import Column, Integer, Float, DateTime, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.base_class import Base

class PaymentMethod(str, enum.Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"

class PaymentStatus(str, enum.Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    FAILED = "failed"
    REFUNDED = "refunded"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    transaction_id = Column(String(255), nullable=True, unique=True) # Para referencias de pasarelas de pago

    # Foreign Keys
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    membership_id = Column(Integer, ForeignKey("memberships.id"), nullable=True) # Puede ser nulo si el pago es por un producto

    # Relaciones
    client = relationship("Client", back_populates="payments")
    membership = relationship("Membership", back_populates="payment")