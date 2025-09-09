# backend/app/dao/permission_dao.py

from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.schemas.permission_schema import PermissionCreate, PermissionUpdate
from typing import List, Optional

class PermissionDAO:
    def get_permission_by_id(self, db: Session, permission_id: int) -> Optional[Permission]:
        """
        Obtiene un permiso específico por su ID.

        Args:
            db (Session): La sesión de la base de datos.
            permission_id (int): El ID del permiso.

        Returns:
            Optional[Permission]: El objeto del permiso si se encuentra, de lo contrario None.
        """
        return db.query(Permission).filter(Permission.id == permission_id).first()

    def get_permission_by_name(self, db: Session, name: str) -> Optional[Permission]:
        """
        Obtiene un permiso específico por su nombre.

        Args:
            db (Session): La sesión de la base de datos.
            name (str): El nombre del permiso.

        Returns:
            Optional[Permission]: El objeto del permiso si se encuentra, de lo contrario None.
        """
        return db.query(Permission).filter(Permission.name == name).first()

    def get_all_permissions(self, db: Session, skip: int = 0, limit: int = 100) -> List[Permission]:
        """
        Obtiene una lista de todos los permisos con paginación.

        Args:
            db (Session): La sesión de la base de datos.
            skip (int): El número de permisos a omitir.
            limit (int): El número máximo de permisos a devolver.

        Returns:
            List[Permission]: Una lista de objetos de permisos.
        """
        return db.query(Permission).offset(skip).limit(limit).all()

    def create_permission(self, db: Session, permission: PermissionCreate) -> Permission:
        """
        Crea un nuevo permiso en la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            permission (PermissionCreate): El objeto con los datos del nuevo permiso.

        Returns:
            Permission: El objeto del permiso recién creado.
        """
        db_permission = Permission(**permission.dict())
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
        return db_permission

    def update_permission(self, db: Session, permission_id: int, permission_update: PermissionUpdate) -> Optional[Permission]:
        """
        Actualiza un permiso existente.

        Args:
            db (Session): La sesión de la base de datos.
            permission_id (int): El ID del permiso a actualizar.
            permission_update (PermissionUpdate): El objeto con los datos a actualizar.

        Returns:
            Optional[Permission]: El objeto del permiso actualizado si existe, de lo contrario None.
        """
        db_permission = self.get_permission_by_id(db, permission_id)
        if db_permission:
            update_data = permission_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_permission, key, value)
            db.commit()
            db.refresh(db_permission)
        return db_permission

    def delete_permission(self, db: Session, permission_id: int) -> Optional[Permission]:
        """
        Elimina un permiso de la base de datos.

        Args:
            db (Session): La sesión de la base de datos.
            permission_id (int): El ID del permiso a eliminar.

        Returns:
            Optional[Permission]: El objeto del permiso eliminado si existe, de lo contrario None.
        """
        db_permission = self.get_permission_by_id(db, permission_id)
        if db_permission:
            db.delete(db_permission)
            db.commit()
        return db_permission