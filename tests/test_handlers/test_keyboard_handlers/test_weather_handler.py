import pytest
from unittest.mock import AsyncMock
from bot.commands.buttons_handlers import town_name_input, town_weather
from bot.commands.keyboards import MENU_KEYBOARD
from bot.commands.states import TownInputStates


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    state = AsyncMock()
    await town_name_input(message, state)
    message.answer.assert_called_with(text="Введите название города", reply_markup=MENU_KEYBOARD)
    state.set_state.assert_called_with(TownInputStates.town_name_input)


async def test_false_town_name():
    message = AsyncMock(text="Абырвалг")
    await town_weather(message)
    message.answer.assert_called_with(
        text="К сожалению, запрошенный вами населённый пункт или область найти не удалось. "
             "Пожалуйста, проверьте, не была ли допущена опечатка."
    )


@pytest.mark.asyncio
async def test_correct_town_name():
    message = AsyncMock(text="Москва")
    await town_weather(message)
    float(message.answer.text)
