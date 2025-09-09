# backend/app/models/setting.py
"""
Define el modelo Setting para almacenar configuraciones clave-valor de la aplicación,
permitiendo modificar el comportamiento del sistema sin necesidad de redesplegar.
"""
import enum
# CORRECCIÓN: Se añade 'Boolean' a la lista de importaciones.
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean
from sqlalchemy.sql import func
from app.db.base_class import Base

class SettingDataType(str, enum.Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    JSON = "json"

class Setting(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, index=True, nullable=False, comment="La clave única de configuración")
    value = Column(Text, nullable=False, comment="El valor de la configuración, almacenado como texto.")
    data_type = Column(Enum(SettingDataType), default=SettingDataType.STRING, nullable=False, comment="El tipo de dato del valor para su correcta interpretación.")
    description = Column(String(255), nullable=True, comment="Explicación de para qué sirve esta configuración.")
    is_editable = Column(Boolean, default=True, comment="Indica si esta configuración puede ser modificada desde una UI de administrador.")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Setting(key='{self.key}')>"

