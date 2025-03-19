from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import exc

from oracle import log
from oracle.routers import api_key, client, core, prediction
from oracle.utils.database import create_db_and_tables

log.info("Application starting up ...")


@asynccontextmanager
async def lifespan(_: FastAPI):
    log.info("Creating database and tables")
    create_db_and_tables()
    yield
    log.info("Application shutting down ...")


app = FastAPI(redirect_slashes=False, lifespan=lifespan)


@app.exception_handler(exc.IntegrityError)
async def integrity_error_exception_handler(_: Request, __: exc.IntegrityError):
    return JSONResponse(
        status_code=409,
        content={"message": "Existing entity already exists"},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=prediction.router)
app.include_router(router=core.router)
app.include_router(router=client.router)
app.include_router(router=api_key.router)
