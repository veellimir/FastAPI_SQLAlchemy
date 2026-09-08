
from core.infrastructure.dao import SQLAlchemyBaseDAO
from core.infrastructure.models import BaseORM


class SQLAlchemyBaseService[T: BaseORM]:
    def __init__(self, repository: SQLAlchemyBaseDAO[T]) -> None:
        self.repository = repository

