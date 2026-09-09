from sqlalchemy.ext.asyncio import AsyncSession

from app.users.domain.exceptions import (
    UserNotFoundException,
)
from app.users.infrastructure.dao import UsersDAO
from app.users.infrastructure.models import UsersORM
from app.users.infrastructure.schemes import (
    UserResponseSchem,
)
from core.domain.service import SQLAlchemyBaseService


class UsersService(SQLAlchemyBaseService[UsersORM]):
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)

    async def get_users_list(self, session: AsyncSession) -> None:
        return await self.dao.get_users_list(session=session)

    async def get_user_by_id(
        self, session: AsyncSession, user_id: int
    ) -> UserResponseSchem | None:
        user = await self.dao.get_user_by_id(
            session=session, user_id=user_id
        )

        if not user:
            raise UserNotFoundException

        return UserResponseSchem.model_validate(user)
