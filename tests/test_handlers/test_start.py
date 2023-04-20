import pytest
from unittest.mock import AsyncMock
from bot.commands.text_commands_handlers import commands_list_command


@pytest.mark.asyncio
async def test_start_handler_en():
    message = AsyncMock(text='start')
    answer = await commands_list_command(message)
    assert answer


@pytest.mark.asyncio
async def test_start_handler_ru():
    message = AsyncMock(text="начать")
    answer = await commands_list_command(message)
    assert answer
