from sqlmodel import SQLModel

import oracle.models.api_key  # noqa: F401
import oracle.models.client  # noqa: F401
from oracle import database_engine


def create_db_and_tables():
    SQLModel.metadata.create_all(database_engine)
