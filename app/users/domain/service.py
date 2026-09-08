from sqlalchemy.ext.asyncio import AsyncSession

from app.users.infrastructure.dao import UsersDAO
from app.users.infrastructure.models import UsersORM
from core.domain.service import SQLAlchemyBaseService


class UsersService(SQLAlchemyBaseService[UsersORM]):
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)

    async def get_users_list(self, session: AsyncSession):
        return await self.dao.get_users_list(session=session)
