from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from oracle import database_engine


def get_session():
    with Session(database_engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
