from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.models import BaseORM

if TYPE_CHECKING:
    from app.lessons.infrastructure.models import LessonsORM


class UsersORM(BaseORM):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(15))
    role: Mapped[str] = mapped_column(String(25))

    lessons: Mapped["LessonsORM"] = relationship(back_populates="users")
