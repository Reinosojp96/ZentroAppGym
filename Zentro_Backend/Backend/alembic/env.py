import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# 🔹 Cargar variables de entorno desde .env
load_dotenv()

# Este es el objeto de configuración de Alembic
config = context.config

# Si existe logging config, cargarlo
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔹 Importa tu Base y tus modelos
from app.db.base_class import Base
from app.models import user, role, client, trainer, incident  # importa todos los modelos que quieras

# target_metadata es usado por 'alembic revision --autogenerate'
target_metadata = Base.metadata

# 🔹 Forzar a usar la URL de la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
