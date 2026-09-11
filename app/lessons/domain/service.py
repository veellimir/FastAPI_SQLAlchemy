from sqlalchemy.ext.asyncio import AsyncSession

from app.lessons.infrastructure.dao import LessonsDAO
from app.lessons.infrastructure.models import LessonsORM
from app.lessons.infrastructure.schemes import (
    LessonResponseSchem,
    LessonsListResponseSchem,
)
from core.domain.service import SQLAlchemyBaseService


class LessonsService(SQLAlchemyBaseService[LessonsORM]):
    def __init__(self, dao: LessonsDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)

    async def get_list_lessons(
        self, session: AsyncSession
    ) -> list[LessonsListResponseSchem]:
        lessons: list[LessonsORM] = await self.dao.get_list_objects(
            session=session
        )
        return [
            LessonsListResponseSchem.model_validate(lesson)
            for lesson in lessons
        ]

    async def get_lesson_by_id(
        self, session: AsyncSession, lesson_id: int
    ) -> LessonResponseSchem | None:
        current_lesson: LessonsORM | None = await self.dao.get_object_by_id(
            session=session, obj_id=lesson_id
        )
        return LessonResponseSchem.model_validate(current_lesson)
