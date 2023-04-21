import os
from typing import Union

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine  # type: ignore
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return _create_async_engine(url, echo=bool(os.getenv('DEBUG')), pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    try:
        with engine.connect() as conn:
            await conn.run_sync(metadata.create_all)
    except AttributeError:
        print("Ошибка подключения к базе данных")


def get_session_maker(engine: AsyncEngine):
    return sessionmaker(engine, class_=AsyncSession)
