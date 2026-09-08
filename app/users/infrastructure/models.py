from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.models import BaseORM


class Users(BaseORM):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(20))
    password: Mapped[str] = mapped_column(String(15))
    role: Mapped[str] = mapped_column(String(25))
