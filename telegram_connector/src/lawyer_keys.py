import telebot
import datetime
import bot_connector

token = '376896577:AAFFKzlziP7rZY4ddHQcAXM2RS2LDkdO_sU'
bot = telebot.TeleBot(token)
print(bot.get_me())


def log(message):
    print("/n========")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nСообщение: {3}".format(message.from_user.first_name,
                                                                     message.from_user.last_name,
                                                                     str(message.from_user.id),
                                                                     message.text))


@bot.message_handler(content_types=["text"])
def handle_text(message):
    # TODO здесь надо вызывать метод из бот конектора и отправлять полученые респонсы из бот конектора.
    response = bot_connector.get_answer()
    for key in response:
        bot.send_message(message.chat.id, response[key])
    # if message.text == "Привет":
    #     bot.send_message(message.chat.id, " Добрый день")
    # elif message.text == "Как дела?":
    #     bot.send_message(message.chat.id, "Прекрасно, а как Ваши?")
    # else:
    #     bot.send_message(message.chat.id, "Я даже не знаю, как на такое ответить!")


@bot.message_handler(comands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")


bot.polling(none_stop=True, interval=50)
