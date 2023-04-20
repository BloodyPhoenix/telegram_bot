from aiogram.fsm.state import StatesGroup, State


class CurrencyConvertationStates(StatesGroup):
    """
    Состояния для обработки логики конфертации валют
    """
    first_currency_input = State()
    currency_amount_input = State()
    second_currency_input = State()


# Возможно, в будущем мы будем запрашивать погоду не только сегодня, но и прогноз на другие дни недели
# Тогда нам пригодится именно StatesGroup
class TownInputStates(StatesGroup):
    """
    Состояния для логики запроса погоды в определённом городе
    """
    town_name_input = State()

