"""
Define la clase Base declarativa de SQLAlchemy de la que heredarán todos los modelos.
"""
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    """
    Clase base para los modelos de SQLAlchemy.
    Genera automáticamente el nombre de la tabla a partir del nombre de la clase.
    """
    id: Any
    __name__: str

    # Genera el nombre de la tabla automáticamente en minúsculas.
    # Ejemplo: la clase "UserRole" se mapeará a la tabla "userrole".
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
