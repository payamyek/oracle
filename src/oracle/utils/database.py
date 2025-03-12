from sqlmodel import SQLModel

from oracle import database_engine
from oracle.models import *  # noqa: F403


def create_db_and_tables():
    SQLModel.metadata.create_all(database_engine)
