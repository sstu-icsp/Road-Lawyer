import requests

# URL по которому расположен бот
BOT_URL = 'http://127.0.0.1:8000/'
# URL по которому можно вызывать метод для получения ответа на сообщение пользователя
GET_ANSWER_URL = BOT_URL + 'api/answer'


def get_answer(chat_id, text):
    """
    Отправляет сообщение в веб-приложение (bot_app)
    :param chat_id: ИД чата с пользователем
    :param text: Сообщение пользователя
    :return: Возвращает ответы от бота
    """
    return requests.get(GET_ANSWER_URL, {'chat_id': chat_id, 'text': text}).json()
