# File: services/setting_service.py
"""
Servicio para settings/configuración persistente. Busca un modelo Setting en
app.models.setting.Setting; si no existe, lanza NotImplementedError indicando cómo
crear una tabla key-value.
"""
from typing import Any, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

try:
    from app.models.setting import Setting
except Exception:
    Setting = None


class SettingService:
    def __init__(self, db: Session):
        self.db = db

    def assert_model(self):
        if Setting is None:
            raise NotImplementedError(
                "No existe app.models.setting.Setting. Crear un modelo Setting simple:\n"
                "class Setting(Base):\n"
                "    __tablename__ = 'settings'\n"
                "    id = Column(Integer, primary_key=True)\n"
                "    key = Column(String, unique=True, index=True)\n"
                "    value = Column(JSON)\n"
            )

    def set(self, key: str, value: Any):
        self.assert_model()
        obj = self.db.query(Setting).filter(Setting.key == key).first()
        if obj:
            obj.value = value
        else:
            obj = Setting(key=key, value=value)
            self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, key: str, default: Optional[Any] = None):
        self.assert_model()
        obj = self.db.query(Setting).filter(Setting.key == key).first()
        if not obj:
            return default
        return obj.value

    def delete(self, key: str):
        self.assert_model()
        obj = self.db.query(Setting).filter(Setting.key == key).first()
        if not obj:
            raise HTTPException(status_code=404, detail="Setting not found")
        self.db.delete(obj)
        self.db.commit()
        return True
