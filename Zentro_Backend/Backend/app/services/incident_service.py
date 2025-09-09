# backend/app/services/incident_service.py
from sqlalchemy.orm import Session
from ..schemas.incident_schema import IncidentCreate, IncidentUpdate
from ..dao.incident_dao import incident_dao

class IncidentService:
    def get_incident(self, db: Session, incident_id: int):
        return incident_dao.get(db, id=incident_id)

    def get_all_incidents(self, db: Session, skip: int = 0, limit: int = 100):
        return incident_dao.get_multi(db, skip=skip, limit=limit)

    def create_incident(self, db: Session, incident_in: IncidentCreate):
        return incident_dao.create(db, obj_in=incident_in)

    def update_incident(self, db: Session, incident_id: int, incident_in: IncidentUpdate):
        db_incident = self.get_incident(db, incident_id)
        if not db_incident:
            return None
        return incident_dao.update(db, db_obj=db_incident, obj_in=incident_in)

    def delete_incident(self, db: Session, incident_id: int):
        db_incident = self.get_incident(db, incident_id)
        if not db_incident:
            return None
        return incident_dao.remove(db, id=incident_id)

incident_service = IncidentService()
