from fastapi import APIRouter

from core.config import settings
from dependecies.annotations import DBSessionDep, UsersServiceDep

router = APIRouter(prefix=settings.api.v1.users, tags=["Пользователи"])


@router.get("/list")
async def get_users_list(session: DBSessionDep, service: UsersServiceDep):
    return await service.get_users_list(session=session)
