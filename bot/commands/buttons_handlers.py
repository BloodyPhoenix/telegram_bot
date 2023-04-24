# Файл, в котором мы храним логику работы через кнопочное меню
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hide_link
from sqlalchemy.orm import sessionmaker

from .keyboards import MENU_KEYBOARD
from .states import TownInputStates, CurrencyConvertationStates
from bot.utils import get_weather, convert_currency, get_picture


async def show_menu(message: Message):
    return message.answer(text="Меню", reply_markup=MENU_KEYBOARD)


async def show_help(message: Message):
    answer = "- Нажмите на кнопку Картинка или введите команду /picture, и я пришлю вам картинку с милым животным ^_^.\n" \
             "- Нажмите на кнопку Погода, или введите команду /weather и название города, и я пришлю вам информацию о " \
             "погоде в этом городе.\n" \
             "- Нажмите на кнопку Конвертация валют или введите команду /convert и количество и обозначение пары " \
             "валют (например, 1000 RUB EUR) или нажмите соответствующую кнопку, и я конвертирую одну валюту в другую " \
             "по текущему курсу ЦБ.\n" \
             "- Нажмите на кнопку Опрос или введите команду /create_poll, и я помогу вам создать опрос в Telegram.\n"
    return message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def town_name_input(message: Message, state: FSMContext):
    answer = "Введите название города"
    await state.set_state(TownInputStates.town_name_input)
    await message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def town_weather(message: Message):
    answer = await get_weather.get_weather(message.text)
    return message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def send_picture(message: Message):
    answer = await get_picture.get_picture(session_maker=sessionmaker())
    if answer:
        await message.answer(text=f'{hide_link(answer)}', parse_mode='HTML', reply_markup=MENU_KEYBOARD)
    else:
        await message.answer(text="Извините, животные не найдены :(", reply_markup=MENU_KEYBOARD)


async def first_currency_input(message: Message, state: FSMContext):
    answer = "Введите обозначение первой валюты"
    await state.set_state(CurrencyConvertationStates.first_currency_input)
    await message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def currency_amount_input(message: Message, state: FSMContext):
    answer = "Введите количество валюты"
    await state.update_data(first=message.text)
    await state.set_state(CurrencyConvertationStates.currency_amount_input)
    await message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def second_currency_input(message: Message, state: FSMContext):
    answer = "Введите обозначение второй валюты"
    try:
        amount = float(message.text)
        await state.update_data(amount=amount)
        await state.set_state(CurrencyConvertationStates.second_currency_input)
        await message.answer(text=answer, reply_markup=MENU_KEYBOARD)
    except ValueError:
        await message.answer(text="Вы ввели не число. Пожалуйста, попробуйте ещё раз", reply_markup=MENU_KEYBOARD)


async def return_convert_currency(message: Message, state: FSMContext):
    data = await state.get_data()
    data['second'] = message.text
    answer = await convert_currency.convert_currency(**data)
    await state.clear()
    await message.answer(text=answer)
