from fastapi import APIRouter

from app.users.infrastructure.schemes import UserResponseSchem
from core.config import settings
from dependecies.annotations import (
    DBSessionDep,
    UsersServiceDep,
)

router = APIRouter(prefix=settings.api.v1.users, tags=["Пользователи"])


@router.get("/list", summary="Получить список пользователей")
async def get_users_list(
    session: DBSessionDep, service: UsersServiceDep
) -> None:
    return await service.get_users_list(session=session)


@router.get("/{user_id}", summary="Получить пользователя по ID")
async def get_user_by_id(
    session: DBSessionDep,
    service: UsersServiceDep,
    user_id: int,
) -> UserResponseSchem | None:
    return await service.get_user_by_id(session=session, user_id=user_id)
