from fastapi import APIRouter, HTTPException
from sqlmodel import select

from oracle.dependencies import SessionDep
from oracle.models.client import Client, ClientCreate, ClientPublic

router = APIRouter(prefix="/api/v1/clients", tags=["Clients"])


@router.post("", response_model=ClientPublic)
def create_client(client: ClientCreate, session: SessionDep):
    db_client = Client.model_validate(client)

    statement = select(Client).where(Client.email == client.email)
    results = session.exec(statement)

    if results.first():
        raise HTTPException(status_code=409, detail=f"Client already exists with the email {client.email}")

    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client
