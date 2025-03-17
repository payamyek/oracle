from fastapi import APIRouter

from oracle.dependencies import SessionDep
from oracle.models.client import Client, ClientCreate, ClientPublic

router = APIRouter(prefix="/api/v1/clients", tags=["Clients"])


@router.post("", response_model=ClientPublic)
def create_client(client: ClientCreate, session: SessionDep):
    db_client = Client.model_validate(client)

    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client
