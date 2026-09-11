from fastapi import APIRouter

from app.lessons.infrastructure.schemes import LessonsListResponseSchem
from core.config import settings
from dependecies.annotations import (
    DBSessionDep,
    LessonServiceDep,
)

router = APIRouter(prefix=settings.api.v1.lessons, tags=["Занятия клуба"])


@router.get("/list", summary="Получить список занятий")
async def get_list_lessons(
    session: DBSessionDep, service: LessonServiceDep
) -> list[LessonsListResponseSchem]:
    return await service.get_list_lessons(session=session)
