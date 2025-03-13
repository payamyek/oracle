from fastapi import APIRouter, HTTPException

from oracle.dependencies import SessionDep
from oracle.models.client import Client

router = APIRouter(
    prefix="/api/v1/clients",
    responses={404: {"description": "Not found"}},
)


@router.post("")
def create_client(client: Client, session: SessionDep) -> Client:
    db_client = Client.model_validate(client)

    if session.get(Client, client.email):
        raise HTTPException(status_code=400, detail=f"Client already exists with the email {client.email}")

    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client
