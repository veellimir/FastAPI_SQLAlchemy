from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DataBase(BaseSettings):
    DATABASE_URL: str
    ECHO_LOG: bool

    class Config:
        env_prefix = ""


class ApiV1Prefix(BaseModel):
    prefix: str = "/api/v1"

    users: str = "/users"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBase
    api: ApiPrefix = ApiPrefix()

    ENV: bool = True

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        extra = "allow"


settings = Settings()
