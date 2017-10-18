class BotConnector:
    def __init__(self):
        bot_url = "http://localhost:8080/"

    def get_answer(self):
        pass
        # TODO здесь надо написать логику для получения ответа у бота. С помощью библиотеки request отправить запрос на
        # бот апи (bot_url + get_answer?chat_id={chat_id}&text={text}".
        # Ответ надо вернуть обратно
        # В ответ на эти сообщения будет приходит json такого типа: [{"text": "some text"}, {"text": "еще текст"}]
