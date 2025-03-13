from fastapi import APIRouter

from oracle.dependencies import SessionDep
from oracle.models.client import Client

router = APIRouter(
    prefix="/api/v1/clients",
    responses={404: {"description": "Not found"}},
)


@router.post("")
def create_client(client: Client, session: SessionDep) -> Client:
    db_client = Client.model_validate(client)
    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client
