import telebot

from telegram_connector import const, bot_service

bot = telebot.TeleBot(const.TOKEN)


def log(message, responses=None):
    """
    Функция для логирования сообщений пользователя. Выводит сообщение пользователя на экран консоли
    :param message: Сообщение пользователя полученое с помощью TeleBot
    :param responses: Ответы полученный от bot_app
    """
    print("\n -------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))

    if responses:
        for response in responses:
            print("Ответ: ", format(response['text']))


@bot.message_handler(commands=['help'])
def handle_text(message):
    """
    Обработчик сообщений пользователя типа команд
    """
    bot.send_message(message.chat.id,
                     "Привет, я дорожный адвокат. Если у тебя возникли проблемы с представителями ГИБДД, то напиши "
                     "мне и я попытаюсь решить твою проблему.")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    """
    Обработчик сообщений пользователя текстового типа
    """
    responses = bot_service.get_answer(message.chat.id, message.text)
    if responses:
        log(message=message, responses=responses)
        for response in responses:
            bot.send_message(message.chat.id, response['text'])


bot.polling(none_stop=True, timeout=100)
