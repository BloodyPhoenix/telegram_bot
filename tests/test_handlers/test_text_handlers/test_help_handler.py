import pytest
from unittest.mock import AsyncMock

from bot.commands import commands_help
from bot.commands.keyboards import MENU_KEYBOARD


@pytest.mark.asyncio
async def test_help_command():
    message = AsyncMock()
    await commands_help(message)
    expected_text = "Я могу помочь вам одним из следующих способов:\n " \
             "- Введите /weather и название города или нажмите на кнопку \"Погода\", и я пришлю вам информацию о" \
             " погоде в этом городе.\n" \
             "- Введите /picture или нажмите на кнопку \"Картинка\", и я пришлю вам картинку с милым животным ^_^\n" \
             "- Введите /create_poll или нажмите на кнопку \"Опрос\", и я помогу вам создать опрос в Telegram.\n" \
             "- Введите /convert, количество и обозначение пары валют (например, 1000 RUR EUR) или нажмите на" \
             " кнопку \"Конвертация валют\", и я конвертирую одну валюту в другую по текущему курсу ЦБ.\n" \
             "Итак, чем могу помочь?"
    message.answer.assert_called_with(text=expected_text, reply_markup=MENU_KEYBOARD)