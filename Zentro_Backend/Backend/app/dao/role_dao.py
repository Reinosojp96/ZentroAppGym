# backend/app/dao/role_dao.py

from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role_schema import RoleCreate, RoleUpdate
from typing import List, Optional

class RoleDAO:
    def get_role_by_id(self, db: Session, role_id: int) -> Optional[Role]:
        """
        Obtiene un rol específico por su ID.

        Args:
            db (Session): La sesión de la base de datos.
            role_id (int): El ID del rol.

        Returns:
            Optional[Role]: El objeto del rol si se encuentra, de lo contrario None.
        """
        return db.query(Role).filter(Role.id == role_id).first()

    def get_role_by_name(self, db: Session, name: str) -> Optional[Role]:
        """
        Obtiene un rol específico por su nombre.

        Args:
            db (Session): La sesión de la base de datos.
            name (str): El nombre del rol.

        Returns:
            Optional[Role]: El objeto del rol si se encuentra, de lo contrario None.
        """
        return db.query(Role).filter(Role.name == name).first()

    def get_all_roles(self, db: Session, skip: int = 0, limit: int = 100) -> List[Role]:
        """
        Obtiene una lista de todos los roles con paginación.

        Args:
            db (Session): La sesión de la base de datos.
            skip (int): El número de roles a omitir.
            limit (int): El número máximo de roles a devolver.

        Returns:
            List[Role]: Una lista de objetos de roles.
        """
        return db.query(Role).offset(skip).limit(limit).all()

    def create_role(self, db: Session, role: RoleCreate) -> Role:
        """
        Crea un nuevo rol en la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            role (RoleCreate): El objeto con los datos del nuevo rol.

        Returns:
            Role: El objeto del rol recién creado.
        """
        db_role = Role(**role.dict())
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role

    def update_role(self, db: Session, role_id: int, role_update: RoleUpdate) -> Optional[Role]:
        """
        Actualiza un rol existente.

        Args:
            db (Session): La sesión de la base de datos.
            role_id (int): El ID del rol a actualizar.
            role_update (RoleUpdate): El objeto con los datos a actualizar.

        Returns:
            Optional[Role]: El objeto del rol actualizado si existe, de lo contrario None.
        """
        db_role = self.get_role_by_id(db, role_id)
        if db_role:
            update_data = role_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_role, key, value)
            db.commit()
            db.refresh(db_role)
        return db_role

    def delete_role(self, db: Session, role_id: int) -> Optional[Role]:
        """
        Elimina un rol de la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            role_id (int): El ID del rol a eliminar.

        Returns:
            Optional[Role]: El objeto del rol eliminado si existe, de lo contrario None.
        """
        db_role = self.get_role_by_id(db, role_id)
        if db_role:
            db.delete(db_role)
            db.commit()
        return db_role