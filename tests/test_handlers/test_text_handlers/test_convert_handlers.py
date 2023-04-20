import asyncio
from asyncio import Future

import pytest
from unittest.mock import AsyncMock, patch

from aiogram.filters import CommandObject

from bot.commands import convert_currency_command


@pytest.mark.asyncio
async def test_convert_currency_no_data():
    message = AsyncMock()
    command = CommandObject('convert')
    await convert_currency_command(message, command)
    message.answer.assert_called_with(text="Вы не ввели никаких данных для работы! Попробуйте ещё раз.")


@pytest.mark.asyncio
async def test_convert_currency_not_enough_data():
    message = AsyncMock()
    command = CommandObject('convert', args='12 RUR')
    await convert_currency_command(message, command)
    message.answer.assert_called_with(text="Вы ввели меньше значений, чем нужно. Попробуйте ещё раз.")


@pytest.mark.asyncio
async def test_convert_currency_no_currency_amount():
    message = AsyncMock()
    command = CommandObject('convert', args='a RUR EUR')
    await convert_currency_command(message, command)
    message.answer.assert_called_with(text="Первым значением должно быть число! попробуйте ещё раз.")


@pytest.mark.asyncio
async def test_convert_currency():
    message = AsyncMock()
    command = CommandObject('convert', args='1000 RUB EUR')
    assert convert_currency_command(message, command)




