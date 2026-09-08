from fastapi import FastAPI, Request

from app.users.domain.service import UsersService
from app.users.infrastructure.dao import UsersDAO


def init_service(app: FastAPI) -> None:
    # DAO
    users_dao = UsersDAO()

    # Services
    users_service = UsersService(users_dao)

    # State
    app.state.user_service = users_service


def get_users_service(request: Request) -> UsersService:
    return request.app.state.user_service
