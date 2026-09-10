from sqlalchemy.ext.asyncio import AsyncSession

from app.users.domain.exceptions import (
    QuestionnaireConflictException,
    UserNotFoundException,
)
from app.users.infrastructure.dao import UsersDAO
from app.users.infrastructure.models import QuestionnaireORM, UsersORM
from app.users.infrastructure.schemes import (
    CreateQuestionnaireSchem,
    UserResponseSchem,
    UsersListResponseSchem,
)
from core.domain.service import SQLAlchemyBaseService


class UsersService(SQLAlchemyBaseService[UsersORM]):
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao
        super().__init__(self.dao)

    async def get_users_list(
        self, session: AsyncSession
    ) -> list[UsersListResponseSchem]:
        users: list[UsersORM] = await self.dao.get_users_list(session=session)

        return [UsersListResponseSchem.model_validate(user) for user in users]

    async def get_user_by_id(
        self, session: AsyncSession, user_id: int
    ) -> UserResponseSchem | None:
        current_user: (
            UserResponseSchem | None
        ) = await self.dao.get_user_by_id(session=session, user_id=user_id)
        if not current_user:
            raise UserNotFoundException

        return UserResponseSchem.model_validate(current_user)

    async def create_questionnaire(
        self,
        session: AsyncSession,
        user_id: int,
        data_questionnaire: CreateQuestionnaireSchem,
    ) -> UserResponseSchem | None:
        current_user: UserResponseSchem | None = await self.get_user_by_id(
            session=session, user_id=user_id
        )

        if not current_user:
            raise UserNotFoundException
        if current_user.questionnaire:
            raise QuestionnaireConflictException

        new_questionnaire: QuestionnaireORM = (
            await self.dao.create_questionnaire(
                session=session,
                user_id=user_id,
                data_questionnaire=data_questionnaire,
            )
        )
        current_user.questionnaire = new_questionnaire

        return UserResponseSchem.model_validate(current_user)
