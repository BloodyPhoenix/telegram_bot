import logging
from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker

from bot.PostgresDB import AnimalsPictures


async def get_picture(session_maker: sessionmaker):
    """
    Функция, возвращающая случайную картинку.
    В текущем исполнении предполагаем, что база выдаёт нам ссылку на картинку.
    Если в базе хранится готовое изображение, то нужно создать временный файл и дать ссыку на него для его загрузки
    в Telegram
    :return: ссылка на картинку
    """
    try:
        async with session_maker() as session:
            async with session.begin():
                link = session.exec(select(AnimalsPictures).order_by(func.random())).first()
                if link:
                    return link
                else:
                    return False
    # TODO Сделать более точную работу с исключениями и подтянуть логгер
    except BaseException as exception:
        print(exception, exception.args)
