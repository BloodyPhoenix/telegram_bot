from unittest.mock import AsyncMock

import pytest
from sqlalchemy.orm import sessionmaker

from bot.utils.get_picture import get_picture


@pytest.mark.asyncio
async def test_no_base():
    session_maker = AsyncMock()
    result = await get_picture(session_maker)
    assert (result == "Извините, животные не найдены :(")

