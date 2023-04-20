import pytest
from unittest.mock import AsyncMock

from aiogram.filters import CommandObject

from bot.commands import weather_command


@pytest.mark.asyncio
async def test_no_town_name():
    message = AsyncMock()
    command = CommandObject('weather')
    await weather_command(message, command)
    message.answer.assert_called_with(text="Вы не ввели название города! Попробуйте ещё раз!")


@pytest.mark.asyncio
async def test_false_town_name():
    message = AsyncMock()
    command = CommandObject('weather', args="Абырвалг")
    await weather_command(message, command)
    message.answer.assert_called_with(
        text="К сожалению, запрошенный вами населённый пункт или область найти не удалось. "
             "Пожалуйста, проверьте, не была ли допущена опечатка."
    )


@pytest.mark.asyncio
async def test_correct_town_name():
    message = AsyncMock()
    command = CommandObject('weather', args="Москва")
    await weather_command(message, command)
    float(message.answer.text)




