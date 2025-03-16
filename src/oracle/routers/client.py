from fastapi import APIRouter, HTTPException
from sqlalchemy import exc

from oracle.dependencies import SessionDep
from oracle.models.client import Client, ClientCreate, ClientPublic

router = APIRouter(prefix="/api/v1/clients", tags=["Clients"])


@router.post("", response_model=ClientPublic)
def create_client(client: ClientCreate, session: SessionDep):
    db_client = Client.model_validate(client)

    try:
        session.add(db_client)
        session.commit()
        session.refresh(db_client)
    except exc.IntegrityError:
        raise HTTPException(status_code=409, detail=f"Client already exists with the email {client.email}")
    except exc.SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__["orig"]))

    return db_client
