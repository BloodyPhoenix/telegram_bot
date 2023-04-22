import pytest
from unittest.mock import AsyncMock
from bot.commands.keyboards import MENU_KEYBOARD
from bot.commands.states import CurrencyConvertationStates
from bot.commands.buttons_handlers import first_currency_input, currency_amount_input, second_currency_input, \
    return_convert_currency


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    state = AsyncMock()
    await first_currency_input(message, state)
    message.answer.assert_called_with(text="Введите обозначение первой валюты", reply_markup=MENU_KEYBOARD)
    state.set_state.assert_called_with(CurrencyConvertationStates.first_currency_input)


@pytest.mark.asyncio
async def test_first_input_handler():
    message = AsyncMock()
    state = AsyncMock()
    await currency_amount_input(message, state)
    message.answer.assert_called_with(text="Введите количество валюты", reply_markup=MENU_KEYBOARD)
    state.set_state.assert_called_with(CurrencyConvertationStates.currency_amount_input)


@pytest.mark.asyncio
async def test_amount_input_handler():
    message = AsyncMock(text='1000')
    state = AsyncMock()
    await second_currency_input(message, state)
    message.answer.assert_called_with(text="Введите обозначение второй валюты", reply_markup=MENU_KEYBOARD)
    state.set_state.assert_called_with(CurrencyConvertationStates.second_currency_input)


@pytest.mark.asyncio
async def test_amount_input_handler():
    message = AsyncMock(text='EUR')
    state = AsyncMock()
    await second_currency_input(message, state)
    message.answer.assert_called_with(
        text="Вы ввели не число. Пожалуйста, попробуйте ещё раз", reply_markup=MENU_KEYBOARD
    )
    state.set_state.assert_not_called()


@pytest.mark.asyncio
async def test_amount_input_handler():
    message = AsyncMock(text='EUR')
    state = AsyncMock()
    await second_currency_input(message, state)
    message.answer.assert_called_with(
        text="Вы ввели не число. Пожалуйста, попробуйте ещё раз", reply_markup=MENU_KEYBOARD
    )
    state.set_state.assert_not_called()