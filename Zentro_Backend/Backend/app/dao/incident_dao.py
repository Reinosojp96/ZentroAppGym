# backend/app/dao/incident_dao.py

from sqlalchemy.orm import Session
from app.models.incident import Incident
from app.schemas.incident_schema import IncidentCreate, IncidentUpdate
from typing import List, Optional

class IncidentDAO:
    def get_incident_by_id(self, db: Session, incident_id: int) -> Optional[Incident]:
        """
        Obtiene un incidente específico por su ID.

        Args:
            db (Session): La sesión de la base de datos.
            incident_id (int): El ID del incidente.

        Returns:
            Optional[Incident]: El objeto del incidente si se encuentra, de lo contrario None.
        """
        return db.query(Incident).filter(Incident.id == incident_id).first()

    def get_all_incidents(self, db: Session, skip: int = 0, limit: int = 100) -> List[Incident]:
        """
        Obtiene una lista de todos los incidentes con paginación.

        Args:
            db (Session): La sesión de la base de datos.
            skip (int): El número de incidentes a omitir.
            limit (int): El número máximo de incidentes a devolver.

        Returns:
            List[Incident]: Una lista de objetos de incidentes.
        """
        return db.query(Incident).order_by(Incident.reported_at.desc()).offset(skip).limit(limit).all()

    def create_incident(self, db: Session, incident: IncidentCreate, reported_by_id: int) -> Incident:
        """
        Crea un nuevo incidente en la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            incident (IncidentCreate): El objeto con los datos del nuevo incidente.
            reported_by_id (int): El ID del usuario que reporta el incidente.

        Returns:
            Incident: El objeto del incidente recién creado.
        """
        db_incident = Incident(
            **incident.dict(),
            reported_by_id=reported_by_id
        )
        db.add(db_incident)
        db.commit()
        db.refresh(db_incident)
        return db_incident

    def update_incident(self, db: Session, incident_id: int, incident_update: IncidentUpdate) -> Optional[Incident]:
        """
        Actualiza un incidente existente.

        Args:
            db (Session): La sesión de la base de datos.
            incident_id (int): El ID del incidente a actualizar.
            incident_update (IncidentUpdate): El objeto con los datos a actualizar.

        Returns:
            Optional[Incident]: El objeto del incidente actualizado si existe, de lo contrario None.
        """
        db_incident = self.get_incident_by_id(db, incident_id)
        if db_incident:
            update_data = incident_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_incident, key, value)
            db.commit()
            db.refresh(db_incident)
        return db_incident

    def delete_incident(self, db: Session, incident_id: int) -> Optional[Incident]:
        """
        Elimina un incidente de la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            incident_id (int): El ID del incidente a eliminar.

        Returns:
            Optional[Incident]: El objeto del incidente eliminado si existe, de lo contrario None.
        """
        db_incident = self.get_incident_by_id(db, incident_id)
        if db_incident:
            db.delete(db_incident)
            db.commit()
        return db_incident