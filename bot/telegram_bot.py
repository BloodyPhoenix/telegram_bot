import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from aioredis import Redis
from dotenv import load_dotenv
from sqlalchemy import URL

from .commands import register_user_commands, commands_list
from .PostgresDB import create_async_engine, get_session_maker, proceed_schemas, AnimalsPictures

# Загрузка переменных окружения.
# Если файл config.env будет перенесён в другую директорию, может потребовтаься более сложная логика.
load_dotenv('config.env')
logging.basicConfig(level=logging.INFO)


async def main() -> None:
    """
    Основная логика работы бота.
    Регистрирует команды, создаёт бота и диспетчер, подюключает PostreSQL и Redis и запускает бота
    :return:
    """
    logging.basicConfig(level=logging.DEBUG)
    bot_commands = []
    for cmd in commands_list.COMMANDS:
        bot_commands.append(BotCommand(command=cmd[0], description=cmd[1]))
    # создаём инстанс Redis.При необходимости задаём переменные в файле config.env
    redis = Redis(
        host=os.getenv('REDIS_HOST') or '127.0.0.1',
        password=os.getenv('REDIS_PASSWORD') or None,
        username=os.getenv('REDIS_USER') or None,
    )
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv("POSTGRES_USER"),
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv("POSTGRES_DB"),
        port=int(os.getenv("POSTGRES_PORT") or 0),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(engine=async_engine, metadata=AnimalsPictures.metadata)
    bot = Bot(token=os.getenv('TOKEN'))
    await bot.set_my_commands(commands=bot_commands)
    dispatcher = Dispatcher(storage=RedisStorage(redis=redis))
    register_user_commands(dispatcher)
    await dispatcher.start_polling(bot)







