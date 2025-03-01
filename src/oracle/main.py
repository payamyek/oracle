from fastapi import FastAPI

from oracle import log
from oracle.routers import predictions

log.info("Application starting up ...")

app = FastAPI()
app.include_router(router=predictions.router)
