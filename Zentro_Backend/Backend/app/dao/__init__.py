
# backend/app/dao/__init__.py
"""
Este archivo inicializa el paquete 'dao' y facilita la importación
de las instancias de los DAOs en otras partes de la aplicación,
principalmente en la capa de servicios.
"""
from .user_dao import user_dao
from .client_dao import client_dao
from .trainer_dao import trainer_dao
from .membership_dao import membership_dao
from .class_dao import gym_class_dao
from .routine_dao import routine_dao
from .nutrition_dao import nutrition_dao
from .store_dao import product_dao
from .incident_dao import incident_dao
from .reception_dao import reception_dao
from .role_dao import RoleDao
from .permission_dao import PermissionDao

# Creación de instancias para ser usadas en la aplicación
user_dao = user_dao()
client_dao = client_dao()
trainer_dao = trainer_dao()
membership_dao = membership_dao()
class_dao = gym_class_dao()
routine_dao = routine_dao()
nutrition_dao = nutrition_dao()
product_dao = product_dao()
incident_dao = incident_dao()
reception_dao = reception_dao()
role_dao = RoleDao()
permission_dao = PermissionDao()
