from contextlib import asynccontextmanager

from fastapi import FastAPI

from oracle import log
from oracle.routers import client, core, prediction
from oracle.utils.database import create_db_and_tables

log.info("Application starting up ...")


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Creating database and tables")
    create_db_and_tables()
    yield
    log.info("Application shutting down ...")


app = FastAPI(redirect_slashes=False, lifespan=lifespan)


app.include_router(router=prediction.router)
app.include_router(router=core.router)
app.include_router(router=client.router)
