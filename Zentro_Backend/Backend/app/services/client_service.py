# backend/app/services/client_service.py
from sqlalchemy.orm import Session
from ..schemas.client_schema import ClientCreate, ClientUpdate
from ..dao.client_dao import client_dao

class ClientService:
    def get_client(self, db: Session, client_id: int):
        return client_dao.get(db, id=client_id)

    def get_all_clients(self, db: Session, skip: int = 0, limit: int = 100):
        return client_dao.get_multi(db, skip=skip, limit=limit)

    def create_client(self, db: Session, client_in: ClientCreate):
        return client_dao.create(db, obj_in=client_in)

    def update_client(self, db: Session, client_id: int, client_in: ClientUpdate):
        db_client = self.get_client(db, client_id)
        if not db_client:
            return None
        return client_dao.update(db, db_obj=db_client, obj_in=client_in)

    def delete_client(self, db: Session, client_id: int):
        db_client = self.get_client(db, client_id)
        if not db_client:
            return None
        return client_dao.remove(db, id=client_id)

client_service = ClientService()
