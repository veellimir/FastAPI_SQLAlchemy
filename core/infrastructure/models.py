import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

INT_PK = Annotated[int, mapped_column(primary_key=True)]

CREATED_AT = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', 'now')"), onupdate=datetime.datetime.now()
    ),
]
UPDATE_AT = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', 'now')"), onupdate=datetime.datetime.now()
    ),
]


class BaseORM(DeclarativeBase):
    id: Mapped[INT_PK]
    created_at: Mapped[CREATED_AT]
    update_at: Mapped[UPDATE_AT]
