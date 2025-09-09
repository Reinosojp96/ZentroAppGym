# backend/app/dao/reception_dao.py

from sqlalchemy.orm import Session
from app.models.reception import Reception
from app.schemas.reception_schema import ReceptionCreate, ReceptionUpdate
from typing import List, Optional

class ReceptionDAO:
    def get_reception_log_by_id(self, db: Session, log_id: int) -> Optional[Reception]:
        """
        Obtiene un registro de recepción específico por su ID.

        Args:
            db (Session): La sesión de la base de datos.
            log_id (int): El ID del registro de recepción.

        Returns:
            Optional[Reception]: El objeto del registro de recepción si se encuentra, de lo contrario None.
        """
        return db.query(Reception).filter(Reception.id == log_id).first()

    def get_all_reception_logs(self, db: Session, skip: int = 0, limit: int = 100) -> List[Reception]:
        """
        Obtiene una lista de todos los registros de recepción con paginación.

        Args:
            db (Session): La sesión de la base de datos.
            skip (int): El número de registros a omitir.
            limit (int): El número máximo de registros a devolver.

        Returns:
            List[Reception]: Una lista de objetos de registros de recepción.
        """
        return db.query(Reception).offset(skip).limit(limit).all()

    def create_reception_log(self, db: Session, reception_log: ReceptionCreate) -> Reception:
        """
        Crea un nuevo registro de recepción en la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            reception_log (ReceptionCreate): El objeto con los datos del nuevo registro.

        Returns:
            Reception: El objeto del registro de recepción recién creado.
        """
        db_reception_log = Reception(**reception_log.dict())
        db.add(db_reception_log)
        db.commit()
        db.refresh(db_reception_log)
        return db_reception_log

    def update_reception_log(self, db: Session, log_id: int, reception_log_update: ReceptionUpdate) -> Optional[Reception]:
        """
        Actualiza un registro de recepción existente.

        Args:
            db (Session): La sesión de la base de datos.
            log_id (int): El ID del registro a actualizar.
            reception_log_update (ReceptionUpdate): El objeto con los datos a actualizar.

        Returns:
            Optional[Reception]: El objeto del registro de recepción actualizado si existe, de lo contrario None.
        """
        db_reception_log = self.get_reception_log_by_id(db, log_id)
        if db_reception_log:
            update_data = reception_log_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_reception_log, key, value)
            db.commit()
            db.refresh(db_reception_log)
        return db_reception_log

    def delete_reception_log(self, db: Session, log_id: int) -> Optional[Reception]:
        """
        Elimina un registro de recepción de la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            log_id (int): El ID del registro a eliminar.

        Returns:
            Optional[Reception]: El objeto del registro de recepción eliminado si existe, de lo contrario None.
        """
        db_reception_log = self.get_reception_log_by_id(db, log_id)
        if db_reception_log:
            db.delete(db_reception_log)
            db.commit()
        return db_reception_log