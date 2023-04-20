import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from aioredis import Redis
from dotenv import load_dotenv

from .commands import register_user_commands, commands_list

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
    bot = Bot(token=os.getenv('TOKEN'))
    await bot.set_my_commands(commands=bot_commands)
    dispatcher = Dispatcher(storage=RedisStorage(redis=redis))
    register_user_commands(dispatcher)
    await dispatcher.start_polling(bot)







