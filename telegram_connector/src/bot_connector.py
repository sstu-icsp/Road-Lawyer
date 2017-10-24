import requests
import telebot

bot_url = "http://localhost:8080/"

class BotConnector:
    def __init__(self):
        bot_url = "http://localhost:8080/"

    def get_answer(message):
        chat_id = message.chat.id
        text = message.text
        response = requests.get(bot_url + "api/view/get_answer?chat_id={0}&text={1}".format(chat_id, text))
        return response.json()
        # TODO здесь надо написать логику для получения ответа у бота. С помощью библиотеки request отправить запрос на
        # бот апи (bot_url + get_answer?chat_id={chat_id}&text={text}".
        # Ответ надо вернуть обратно
        # В ответ на эти сообщения будет приходит json такого типа: [{"text": "some text"}, {"text": "еще текст"}
