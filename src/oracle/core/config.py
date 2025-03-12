from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url = SettingsConfigDict(env_prefix="ORACLE_")
