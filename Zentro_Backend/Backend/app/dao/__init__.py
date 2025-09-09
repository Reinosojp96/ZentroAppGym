
# backend/app/dao/__init__.py
"""
Este archivo inicializa el paquete 'dao' y facilita la importación
de las instancias de los DAOs en otras partes de la aplicación,
principalmente en la capa de servicios.
"""
from .user_dao import UserDao
from .client_dao import ClientDao
from .trainer_dao import TrainerDao
from .membership_dao import MembershipDao
from .class_dao import ClassDao
from .routine_dao import RoutineDao
from .nutrition_dao import NutritionDao
from .store_dao import ProductDao
from .incident_dao import IncidentDao
from .reception_dao import ReceptionDao
from .role_dao import RoleDao
from .permission_dao import PermissionDao

# Creación de instancias para ser usadas en la aplicación
user_dao = UserDao()
client_dao = ClientDao()
trainer_dao = TrainerDao()
membership_dao = MembershipDao()
class_dao = ClassDao()
routine_dao = RoutineDao()
nutrition_dao = NutritionDao()
product_dao = ProductDao()
incident_dao = IncidentDao()
reception_dao = ReceptionDao()
role_dao = RoleDao()
permission_dao = PermissionDao()
