from fastapi import APIRouter, HTTPException
from sqlmodel import select

from oracle.dependencies import SessionDep
from oracle.models.client import Client, ClientCreate, ClientPublic

router = APIRouter(
    prefix="/api/v1/clients",
)


@router.post("")
def create_client(client: ClientCreate, session: SessionDep) -> ClientPublic:
    db_client = Client.model_validate(client)

    statement = select(Client).where(Client.email == client.email)
    results = session.exec(statement)

    if results.first():
        raise HTTPException(status_code=400, detail=f"Client already exists with the email {client.email}")

    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return ClientPublic.model_validate(db_client)
