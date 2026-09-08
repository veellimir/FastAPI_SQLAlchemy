import datetime
import json
from collections.abc import AsyncGenerator
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from .config import settings

engine = create_async_engine(
    settings.connect_db,
    echo=False,
    json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False, default=str),
)

async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=True,
    autoflush=True
)





async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session_maker.begin() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
