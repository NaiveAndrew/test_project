# Импортируем необходимые библиотеки, классы и переменные
from extensions import APIException
from extensions import CryptoCompareAPI
from currencie_names import CURRENCIES
import telebot
import requests
import json

# Читаем токен телеграм бота из config.py
from config import TOKEN

# Создаем объект бота с помощью библиотеки pyTelegramBotAPI
bot = telebot.TeleBot(TOKEN)


# Определяем функцию для обработки команды /start или /help
@bot.message_handler(commands=["start", "help"])
def start_help(message):
    # Отправляем пользователю инструкции по применению бота
    bot.send_message(message.chat.id, "Привет! Я бот для конвертации валют. Чтобы узнать цену валюты, отправь мне сообщение в виде:\n"
    "<имя валюты цену которой хочешь узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>\n"
    "Например: евро доллар 10\n"
    "Чтобы узнать все доступные валюты, отправь мне команду /values")

# Определяем функцию для обработки команды /values
@bot.message_handler(commands=["values"])
def values(message):
    # Формируем список доступных валют в читаемом виде
    text = "Доступные валюты:\n"
    for key in CURRENCIES.keys():
        text += key + "\n"
    # Отправляем пользователю список доступных валют
    bot.send_message(message.chat.id, text)

# Определяем функцию для обработки текстовых сообщений от пользователя
@bot.message_handler(content_types=["text"])
def convert(message):
    # Переводим сообщение пользователя в нижний регистр
    message.text = message.text.lower()
    # Пытаемся разобрать сообщение пользователя на три компонента
    try:
        # Разделяем сообщение по пробелам
        params = message.text.split(" ")
        # Проверяем, что получили ровно три компонента
        if len(params) != 3:
            # Если нет, вызываем исключение
            raise APIException("Неверное количество параметров")
        # Присваиваем переменным имена валют и количество
        base, quote, amount = params
        # Проверяем, что введенные валюты доступны для конвертации
        if base not in CURRENCIES or quote not in CURRENCIES:
            # Если нет, вызываем исключение
            raise APIException("Неверное имя валюты")
        # Проверяем, что введенное количество является числом
        try:
            amount = float(amount)
        except ValueError:
            # Если нет, вызываем исключение
            raise APIException("Неверное количество валюты")
        # Вызываем статический метод класса CryptoCompareAPI для получения цены валюты
        result = CryptoCompareAPI.get_price(CURRENCIES[base], CURRENCIES[quote], amount)
        # Формируем текст ответа с результатом конвертации
        text = f"{amount} {base} в {quote} = {result}"
    # Обрабатываем возможные исключения
    except APIException as e:
        # Отправляем пользователю текст ошибки из исключения
        bot.send_message(message.chat.id, e.message)
    except Exception as e:
        # Отправляем пользователю текст неизвестной ошибки с указанием типа ошибки
        bot.send_message(message.chat.id, f"Неизвестная ошибка: {e.__class__.__name__}")
    else:
        # Отправляем пользователю текст ответа с результатом конвертации
        bot.send_message(message.chat.id, text)

# Запускаем бота в режиме опроса сервера Telegram
bot.polling(none_stop=True)