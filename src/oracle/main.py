from fastapi import FastAPI

from oracle import log
from oracle.routers import core, prediction

log.info("Application starting up ...")

app = FastAPI(redirect_slashes=False)


app.include_router(router=prediction.router)
app.include_router(router=core.router)
