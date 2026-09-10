from app.lessons.infrastructure.dao import LessonsDAO
from app.lessons.infrastructure.models import LessonsORM
from core.domain.service import SQLAlchemyBaseService


class LessonsService(SQLAlchemyBaseService[LessonsORM]):
    def __init__(self, dao: LessonsDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)
