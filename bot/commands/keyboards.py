from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

MENU_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
        InlineKeyboardButton(text="Погода", callback_data="town_name_input"),
        KeyboardButton(text="Картинка", callback_data='picture'),
        KeyboardButton(text="Создать опрос",  request_poll=True)
        ],
        [InlineKeyboardButton(text="Конвертация валют", callback_data='convert_first_name'),],
        [KeyboardButton(text="Помощь", callback_data='gethelp')]
    ],
    resize_keyboard=True
)
