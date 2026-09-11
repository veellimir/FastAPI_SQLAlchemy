from sqlalchemy.ext.asyncio import AsyncSession

from app.lessons.infrastructure.dao import LessonsDAO
from app.lessons.infrastructure.models import LessonsORM
from app.lessons.infrastructure.schemes import LessonsListResponseSchem
from core.domain.service import SQLAlchemyBaseService


class LessonsService(SQLAlchemyBaseService[LessonsORM]):
    def __init__(self, dao: LessonsDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)

    async def get_list_lessons(
        self, session: AsyncSession
    ) -> list[LessonsListResponseSchem]:
        lessons: list[object] = await self.dao.get_list_objects(
            session=session
        )
        return [
            LessonsListResponseSchem.model_validate(lesson)
            for lesson in lessons
        ]
