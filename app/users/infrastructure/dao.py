from sqlalchemy.ext.asyncio import AsyncSession

from app.users.infrastructure.models import UsersORM
from core.infrastructure.dao import SQLAlchemyBaseDAO


class UsersDAO(SQLAlchemyBaseDAO):
    def __init__(self):
        self.model = UsersORM
        super().__init__(UsersORM)

    async def get_users_list(self, session: AsyncSession):
        pass
