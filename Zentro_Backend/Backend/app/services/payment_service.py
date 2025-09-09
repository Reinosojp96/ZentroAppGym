# File: services/payment_service.py
"""
Servicio de pagos (stub / integrador)
Este módulo proporciona una clase PaymentService con métodos para crear intents de pago
y registrar pagos. Está pensado para integrarse con Stripe/PayPal u otro gateway.
Para el registro en DB espera un modelo `Payment` en `app.models.payment`. Si no existe,
la parte de persistencia será un stub que lanza NotImplementedError con instrucciones.
"""
from typing import Optional, Dict, Any, List
from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
import datetime

try:
    from app.models.payment import Payment  # optional, may not exist
except Exception:
    Payment = None


class PaymentService:
    def __init__(self, db: Session):
        self.db = db

    def create_payment_intent(self, amount_cents: int, currency: str = "usd", metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Crear un intento de pago en el gateway.
        **Implementación:** aquí devolvemos un 'intent' simulado con id y client_secret.
        Reemplazar por integración real con Stripe/PayPal.
        """
        if amount_cents <= 0:
            raise HTTPException(status_code=400, detail="amount must be > 0")

        intent = {
            "id": f"pi_{uuid.uuid4().hex}",
            "amount": amount_cents,
            "currency": currency,
            "client_secret": uuid.uuid4().hex,
            "metadata": metadata or {},
            "status": "requires_payment_method",
            "created_at": datetime.datetime.utcnow().isoformat(),
        }
        return intent

    def record_payment(self, intent_id: str, amount_cents: int, currency: str, payload: Dict[str, Any]) -> Any:
        """Registra un pago en la base de datos si existe el modelo Payment.
        Si no existe, devuelve la representación que *debería* guardarse.
        """
        record = {
            "intent_id": intent_id,
            "amount": amount_cents,
            "currency": currency,
            "payload": payload,
            "recorded_at": datetime.datetime.utcnow(),
        }

        if Payment is None:
            # No hay modelo Payment en el proyecto. Devolvemos el record y
            # documentamos cómo proceder.
            raise NotImplementedError(
                "No existe app.models.payment.Payment. Crear un modelo Payment o adaptar record_payment para usar el DAO/tabla existente.\n"
                "Ejemplo de modelo esperado:\n" 
                "class Payment(Base):\n"
                "    __tablename__ = 'payments'\n"
                "    id = Column(Integer, primary_key=True)\n"
                "    intent_id = Column(String, unique=True, index=True)\n"
                "    amount = Column(Integer)\n"
                "    currency = Column(String)\n"
                "    payload = Column(JSON)\n"
                "    recorded_at = Column(DateTime)\n"
            )

        db_obj = Payment(
            intent_id=intent_id,
            amount=amount_cents,
            currency=currency,
            payload=payload,
            recorded_at=record["recorded_at"],
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_payments(self, limit: int = 100, offset: int = 0) -> List[Any]:
        if Payment is None:
            raise NotImplementedError("No existe modelo Payment. Crear app.models.payment.Payment para listar pagos.")
        return self.db.query(Payment).offset(offset).limit(limit).all()
