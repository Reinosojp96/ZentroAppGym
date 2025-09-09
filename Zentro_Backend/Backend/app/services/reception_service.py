# File: services/reception_service.py
"""
Servicio para recepciones: check-in de clientes, listar entradas, validar membresía.
Asume existencia de app.models.reception.Reception y app.models.client.Client
y app.models.membership.Membership para validar estados.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
import datetime

try:
    from app.models.reception import Reception
    from app.models.client import Client
    from app.models.membership import Membership
except Exception:
    Reception = None
    Client = None
    Membership = None


class ReceptionService:
    def __init__(self, db: Session):
        self.db = db

    def checkin_client(self, client_id: int, by_user_id: Optional[int] = None):
        """Registra un check-in para un cliente si su membresía está activa.
        Devuelve el objeto Reception creado.
        """
        if Client is None or Reception is None:
            raise NotImplementedError("Faltan modelos Reception/Client en app.models")

        client = self.db.query(Client).get(client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        # validar membresía si existe
        if Membership is not None:
            membership = self.db.query(Membership).filter(Membership.client_id == client_id).order_by(Membership.expires_at.desc()).first()
            if not membership or getattr(membership, 'is_active', None) is False:
                raise HTTPException(status_code=403, detail="Cliente no tiene membresía activa")

        rec = Reception(client_id=client_id, checkin_at=datetime.datetime.utcnow(), by_user_id=by_user_id)
        self.db.add(rec)
        self.db.commit()
        self.db.refresh(rec)
        return rec

    def list_checkins(self, limit: int = 100, offset: int = 0) -> List[Any]:
        if Reception is None:
            raise NotImplementedError("Falta modelo app.models.reception.Reception")
        return self.db.query(Reception).order_by(Reception.checkin_at.desc()).offset(offset).limit(limit).all()

    def get_checkin(self, checkin_id: int):
        if Reception is None:
            raise NotImplementedError("Falta modelo app.models.reception.Reception")
        rec = self.db.query(Reception).get(checkin_id)
        if not rec:
            raise HTTPException(status_code=404, detail="Check-in not found")
        return rec