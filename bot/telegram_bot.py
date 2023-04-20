import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from aioredis import Redis
from .commands import register_user_commands, commands_list

API_TOKEN = '6137710823:AAFS_CaRsoacW6bFImQFh8_peQTCKix5RVw'

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    """
    Основная логика работы бота.
    Регистрирует команды, создаёт бота и диспетчер, запускает бота
    :return:
    """
    logging.basicConfig(level=logging.DEBUG)
    bot_commands = []
    for cmd in commands_list.COMMANDS:
        bot_commands.append(BotCommand(command=cmd[0], description=cmd[1]))
    # при необходимости задаём порт и пароль для подключения базы данных при создании инстанса Redis
    redis = Redis()
    bot = Bot(API_TOKEN)
    await bot.set_my_commands(commands=bot_commands)
    dispatcher = Dispatcher(storage=RedisStorage(redis=redis))
    register_user_commands(dispatcher)
    await dispatcher.start_polling(bot)







