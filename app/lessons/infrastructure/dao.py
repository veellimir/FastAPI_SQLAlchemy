from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.lessons.infrastructure.models import LessonsORM
from core.infrastructure.dao import SQLAlchemyBaseDAO


class LessonsDAO(SQLAlchemyBaseDAO):
    def __init__(self) -> None:
        self.model = LessonsORM
        super().__init__(LessonsORM)

    async def patch_lesson_by_id(
        self,
        session: AsyncSession,
        lesson: LessonsORM,
        data_lesson: dict[str, Any],
    ) -> LessonsORM:
        for field, value in data_lesson.items():
            setattr(lesson, field, value)

        await session.flush()
        return lesson
