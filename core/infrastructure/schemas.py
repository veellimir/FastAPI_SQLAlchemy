from pydantic import BaseModel, ConfigDict


class BaseSchem(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseResponseSchem(BaseSchem):
    id: int
