from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DataBase(BaseSettings):
    DATABASE_URL: str
    ECHO_LOG: bool

    class Config:
        env_prefix = ""


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBase

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        extra = "allow"


settings = Settings()
