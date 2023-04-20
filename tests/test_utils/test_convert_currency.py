import pytest
from bot.utils.convert_currency import convert_currency


@pytest.mark.asyncio
async def test_wrong_value_first():
    result = await convert_currency(1000, 'C', "EUR")
    expected_answer = 'Извините, валюта C не найдена. Пожалуйста, уточните запрос.'
    assert (result == expected_answer)


@pytest.mark.asyncio
async def test_wrong_value_second():
    result = await convert_currency(1000, 'EUR', "R")
    expected_answer = 'Извините, валюта R не найдена. Пожалуйста, уточните запрос.'
    assert (result == expected_answer)


@pytest.mark.asyncio
async def test_correct_input():
    result = await convert_currency(1000, 'EUR', "RUB")
    assert ('По курсу' in result)

