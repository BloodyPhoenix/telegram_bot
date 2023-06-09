__all__ = ['commands_list', 'register_user_commands', 'states', 'keyboards']

from aiogram import Router, F
from aiogram.filters import Command
from bot.commands.states import TownInputStates, CurrencyConvertationStates
from bot.commands.text_commands_handlers import commands_help, weather_command, convert_currency_command
from bot.commands.buttons_handlers import show_menu, send_picture, town_name_input, town_weather, \
    first_currency_input, show_help, currency_amount_input, second_currency_input, return_convert_currency


def register_user_commands(router: Router) -> None:
    initial_commands = ['start', 'menu']
    help_commands = ['help', 'commands']
    router.message.register(show_menu, Command(commands=initial_commands))
    router.message.register(commands_help, Command(commands=help_commands)),
    router.message.register(convert_currency_command, Command(commands=['convert', ]))
    router.message.register(weather_command, Command(commands=['weather',]))
    router.message.register(show_help, F.text == "Помощь")
    router.message.register(send_picture, F.text == "Картинка")
    router.message.register(first_currency_input, F.text == "Конвертация валют")
    router.message.register(town_name_input, F.text == "Погода")
    router.message.register(town_weather, TownInputStates.town_name_input)
    router.message.register(currency_amount_input, CurrencyConvertationStates.first_currency_input)
    router.message.register(second_currency_input, CurrencyConvertationStates.currency_amount_input)
    router.message.register(return_convert_currency, CurrencyConvertationStates.second_currency_input)


