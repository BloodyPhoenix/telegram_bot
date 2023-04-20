import pytest
from bot.utils.get_weather import get_weather


@pytest.mark.asyncio
async def test_get_weather_false_town():
    result = await get_weather("Абырвалг")
    expected_answer = "К сожалению, запрошенный вами населённый пункт или область найти не удалось. " \
                      "Пожалуйста, проверьте, не была ли допущена опечатка."
    assert (result == expected_answer)


@pytest.mark.asyncio
async def test_get_weather():
    result = await get_weather("Москва")
    assert (type(result) == float)



