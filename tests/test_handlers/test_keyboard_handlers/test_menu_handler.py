import pytest
from unittest.mock import AsyncMock
from bot.commands.buttons_handlers import show_menu
from bot.commands.keyboards import MENU_KEYBOARD


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    state = AsyncMock()
    await show_menu(message, state)
    message.answer.assert_called_with(text="Меню", reply_markup=MENU_KEYBOARD)