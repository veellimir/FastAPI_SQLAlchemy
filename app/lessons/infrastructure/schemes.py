from core.infrastructure.schemas import BaseResponseSchem
from core.infrastructure.typing import CustomDate


class LessonsListResponseSchem(BaseResponseSchem):
    title: str


class LessonResponseSchem(LessonsListResponseSchem):
    description: str | None = None
    start_date: CustomDate
    end_date: CustomDate
