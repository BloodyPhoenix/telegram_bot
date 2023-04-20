from pygismeteo import Gismeteo


async def get_weather(town_name: str):
    """
    Функция, которая возвращает информацию о погоде в городе
    :param town_name: Название города
    :return: Температура вграудсах Цельсия
    """
    gismeteo = Gismeteo()
    search_results = gismeteo.search.by_query(town_name)
    if search_results:
         city_id = search_results[0].id
         current = gismeteo.current.by_id(city_id)
         return current.temperature.air.c
    return("К сожалению, запрошенный вами населённый пункт или область найти не удалось. "
           "Пожалуйста, проверьте, не была ли допущена опечатка.")
