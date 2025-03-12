from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field(default="")
    model_config = SettingsConfigDict(env_prefix="ORACLE_")
