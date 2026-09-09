from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.users.infrastructure.models import UsersORM
from core.infrastructure.dao import SQLAlchemyBaseDAO


class UsersDAO(SQLAlchemyBaseDAO):
    def __init__(self) -> None:
        self.model = UsersORM
        super().__init__(UsersORM)

    async def get_users_list(self, session: AsyncSession) -> None:
        pass

    async def get_user_by_id(
        self, session: AsyncSession, user_id: int
    ) -> UsersORM | None:
        stmt = (
            select(self.model)
            .options(joinedload(self.model.questionnaire))
            .where(self.model.id == user_id)
        )

        result = await session.execute(stmt)
        return result.scalar_one_or_none()
