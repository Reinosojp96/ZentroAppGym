# backend/app/dao/configuration_dao.py

from sqlalchemy.orm import Session
from app.models.setting import Configuration # Asumiendo que tienes un modelo 'configuration.py'
from app.schemas.setting_schema import ConfigurationCreate, ConfigurationUpdate # Asumiendo que tienes un 'configuration_schema.py'
from typing import List, Optional

class ConfigurationDAO:
    def get_config_by_key(self, db: Session, key: str) -> Optional[Configuration]:
        """
        Obtiene un valor de configuración específico por su clave.

        Args:
            db (Session): La sesión de la base de datos.
            key (str): La clave de la configuración a buscar.

        Returns:
            Optional[Configuration]: El objeto de configuración si se encuentra, de lo contrario None.
        """
        return db.query(Configuration).filter(Configuration.key == key).first()

    def get_all_configs(self, db: Session, skip: int = 0, limit: int = 100) -> List[Configuration]:
        """
        Obtiene una lista de todas las configuraciones con paginación.

        Args:
            db (Session): La sesión de la base de datos.
            skip (int): El número de configuraciones a omitir.
            limit (int): El número máximo de configuraciones a devolver.

        Returns:
            List[Configuration]: Una lista de objetos de configuración.
        """
        return db.query(Configuration).offset(skip).limit(limit).all()

    def create_config(self, db: Session, config: ConfigurationCreate) -> Configuration:
        """
        Crea una nueva entrada de configuración en la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            config (ConfigurationCreate): El objeto con los datos de la nueva configuración.

        Returns:
            Configuration: El objeto de configuración recién creado.
        """
        db_config = Configuration(**config.dict())
        db.add(db_config)
        db.commit()
        db.refresh(db_config)
        return db_config

    def update_config(self, db: Session, key: str, config_update: ConfigurationUpdate) -> Optional[Configuration]:
        """
        Actualiza una configuración existente por su clave.

        Args:
            db (Session): La sesión de la base de datos.
            key (str): La clave de la configuración a actualizar.
            config_update (ConfigurationUpdate): El objeto con los nuevos datos.

        Returns:
            Optional[Configuration]: El objeto de configuración actualizado si existe, de lo contrario None.
        """
        db_config = self.get_config_by_key(db, key)
        if db_config:
            # Solo actualiza el valor, ya que la clave es el identificador.
            db_config.value = config_update.value
            db.commit()
            db.refresh(db_config)
        return db_config

    def delete_config(self, db: Session, key: str) -> Optional[Configuration]:
        """
        Elimina una configuración de la base de datos por su clave.

        Args:
            db (Session): La sesión de la base de datos.
            key (str): La clave de la configuración a eliminar.

        Returns:
            Optional[Configuration]: El objeto de la configuración eliminada si existía, de lo contrario None.
        """
        db_config = self.get_config_by_key(db, key)
        if db_config:
            db.delete(db_config)
            db.commit()
        return db_config