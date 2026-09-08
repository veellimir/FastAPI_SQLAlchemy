from core.infrastructure.models import BaseORM


class SQLAlchemyBaseDAO[T: BaseORM]:
    def __init__(self, model: type[T]):
        self.model = model

