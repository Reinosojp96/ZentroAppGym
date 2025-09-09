# backend/app/dao/client_dao.py
"""
DAO para operaciones de base de datos relacionadas con el modelo Client.
"""
from app.dao.dao_base import DaoBase
from app.models.client import Client
from app.schemas.client_schema import ClientCreate, ClientUpdate

class ClientDao(DaoBase[Client, ClientCreate, ClientUpdate]):
    def __init__(self):
        super().__init__(Client)

    # Aquí puedes añadir métodos específicos para clientes, por ejemplo:
    # def find_by_name(self, db: Session, name: str) -> List[Client]:
    #     return db.query(Client).filter(Client.full_name.ilike(f"%{name}%")).all()
