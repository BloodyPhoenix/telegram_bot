# Файл, в котором мы храним логику работы через кнопочное меню
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from .keyboards import MENU_KEYBOARD
from .states import TownInputStates


async def show_menu(message: Message, state: FSMContext):
    return message.answer(text="Меню", reply_markup=MENU_KEYBOARD)


async def show_help(message: Message):
    answer = "- Нажмите на кнопку Картинка или введите команду /picture, и я пришлю вам картинку с милым животным ^_^.\n" \
             "- Нажмите на кнопку Погода, или введите команду /weather и название города, и я пришлю вам информацию о " \
             "погоде в этом городе.\n" \
             "- Нажмите на кнопку Конвертация валют или введите команду /convert и количество и обозначение пары " \
             "валют (например, 1000 RUR EUR) или нажмите соответствующую кнопку, и я конвертирую одну валюту в другую " \
             "по текущему курсу ЦБ.\n" \
             "- Нажмите на кнопку Опрос или введите команду /create_poll, и я помогу вам создать опрос в Telegram.\n"
    return message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def town_name_input(message: Message, state: FSMContext):
    answer = "Введите название города"
    await message.answer(text=answer, reply_markup=MENU_KEYBOARD)
    await state.set_state(TownInputStates.town_name_input)


async def town_weather(message: Message):
    answer = "Извините,я пока не умею этого делать"
    return message.answer(text=answer, reply_markup=MENU_KEYBOARD)


async def send_picture():
    pass


async def first_currency_input():
    pass


async def currency_amount_input():
    pass


async def second_currency_input():
    pass


async def convet_currency():
    pass
