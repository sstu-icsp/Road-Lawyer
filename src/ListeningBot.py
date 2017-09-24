import telebot

token = '376896577:AAFFKzlziP7rZY4ddHQcAXM2RS2LDkdO_sU'
bot = telebot.TeleBot(token)
print(bot.get_me())

def log(message):
    print("/n========")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nСообщение: {3}".format(message.from_user.first_name,
                                                                     message.from_user.last_name,
                                                                     str(message.from_user.id),
                                                                     message.text))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    log(message)
    if message.text == "Привет" :
        bot.send_message(message.chat.id," Добрый день")
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id,"Прекрасно, а как Ваши?")
    else: bot.send_message(message.chat.id,"Я даже не знаю, как на такое ответить!")

@bot.message_handler(comands = ['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")

bot.polling(none_stop=True, interval=0)

