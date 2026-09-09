from core.infrastructure.models import BaseORM


class SQLAlchemyBaseDAO[T: BaseORM]:
    def __init__(self, model: type[T]) -> None:
        self.model = model

    async def get_list(self) -> None:
        pass
