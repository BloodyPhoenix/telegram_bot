import requests
from dateutil.parser import parse


async def convert_currency(amount: float, first: str, second: str):
    """
    Функция для ковертации валют по текущему курсу. Использует Exchange Rates API
    :param amount: количество валюты для обмена
    :param first: валюта, которую будет конвертировать
    :param second: валюта, в которую будем конвертировать
    :return: строка с результатом конвертации
    """
    url = f"https://open.er-api.com/v6/latest/{first}"
    try:
        data = requests.get(url).json()
    except ConnectionError:
        return "Извините, я не могу подключиться к сервису с данными по текузим курсам валют. Попробуйте позже"
    if data["result"] == "success":
        exchange_rates = data["rates"]
        if not second in exchange_rates:
            return f'Извините, валюта {second} не найдена. Пожалуйста, уточните запрос.'
        # TODO Возможно, стоит сделать рефакторинг даты и времени, чтобы она красивее выглядела.
        course_update = parse(data["time_last_update_utc"])
        result = exchange_rates[second] * amount
        return f'По курсу на {course_update} {amount} {first} ковертируются в {result} {second}'
    else:
        return f'Извините, валюта {first} не найдена. Пожалуйста, уточните запрос.'