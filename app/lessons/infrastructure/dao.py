from app.lessons.infrastructure.models import LessonsORM
from core.infrastructure.dao import SQLAlchemyBaseDAO


class LessonsDAO(SQLAlchemyBaseDAO):
    def __init__(self) -> None:
        self.model = LessonsORM
        super().__init__(LessonsORM)
