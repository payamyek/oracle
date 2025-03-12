import structlog
from sqlmodel import create_engine

from oracle.config import Settings

log = structlog.get_logger()
settings = Settings()

database_engine = create_engine(settings.database_url)
