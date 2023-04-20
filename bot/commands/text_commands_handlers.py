# Файл, в котором мы храним функции, отвчающие на текстовые командыhandlers

from aiogram.filters import CommandObject
from aiogram.types import Message
from bot.commands.keyboards import MENU_KEYBOARD
from bot.utils.convert_currency import convert_currency
from bot.utils.get_weather import get_weather


async def commands_help(message: Message):
    """
    Функция, возвращающая список возможных команд
    :return: строка со справкой
    """
    answer = "Я могу помочь вам одним из следующих способов:\n " \
             "- Введите /weather и название города или нажмите на кнопку \"Погода\", и я пришлю вам информацию о" \
             " погоде в этом городе.\n" \
             "- Введите /picture или нажмите на кнопку \"Картинка\", и я пришлю вам картинку с милым животным ^_^\n" \
             "- Введите /create_poll или нажмите на кнопку \"Опрос\", и я помогу вам создать опрос в Telegram.\n" \
             "- Введите /convert, количество и обозначение пары валют (например, 1000 RUR EUR) или нажмите на" \
             " кнопку \"Конвертация валют\", и я конвертирую одну валюту в другую по текущему курсу ЦБ.\n" \
             "Итак, чем могу помочь?"
    await message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def weather_command(message: Message, command: CommandObject):
    if command.args:
        weather_info = await get_weather(command.args)
        await message.answer(text=str(weather_info))
    else:
        await message.answer(text="Вы не ввели название города! Попробуйте ещё раз!")


async def send_picture_command(message: Message):
    await message.answer(text="Извините, я ещё не умею этого делать.")


async def convert_currency_command(message: Message, command: CommandObject):
    if not command.args:
        await message.answer(text="Вы не ввели никаких данных для работы! Попробуйте ещё раз.")
    else:
        data = command.args.split()
        if len(data) < 3:
            await message.answer(text="Вы ввели меньше значений, чем нужно. Попробуйте ещё раз.")
        else:
            try:
                float(data[0])
                convertation_result = await convert_currency(float(data[0]), data[1], data[2])
                await message.answer(text=convertation_result)
            except ValueError:
                await message.answer(text="Первым значением должно быть число! попробуйте ещё раз.")

