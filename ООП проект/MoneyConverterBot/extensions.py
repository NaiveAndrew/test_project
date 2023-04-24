import requests
import json

# Создаем класс для обработки ошибок API
class APIException(Exception):
    # Конструктор класса принимает сообщение об ошибке
    def __init__(self, message):
        # Вызываем конструктор базового класса Exception
        super().__init__(message)
        # Сохраняем сообщение об ошибке в атрибуте
        self.message = message

# Создаем класс для работы с API курсов валют
class CryptoCompareAPI:
    # Статический метод для получения цены валюты
    @staticmethod
    def get_price(base, quote, amount):
        # Формируем URL запроса к API
        url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
        # Отправляем запрос и получаем ответ
        response = requests.get(url)
        # Проверяем статус ответа
        if response.status_code == 200:
            # Преобразуем ответ в JSON формат
            data = json.loads(response.content)
            # Проверяем наличие нужной валюты в ответе
            if quote in data:
                # Возвращаем цену валюты, умноженную на количество
                return data[quote] * amount
            else:
                # Если валюта не найдена, вызываем исключение
                raise APIException(f"Валюта {quote} не доступна для конвертации")
        else:
            # Если статус ответа не 200, вызываем исключение
            raise APIException(f"Ошибка при обращении к API: {response.status_code}")