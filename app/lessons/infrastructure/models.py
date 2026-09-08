from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure import BaseORM

if TYPE_CHECKING:
    from app.users.infrastructure.models import UsersORM


class LessonsORM(BaseORM):
    __tablename__ = "lessons"

    title: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["UsersORM"] = relationship(
        back_populates="lessons"
    )


