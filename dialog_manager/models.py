from django.db import models


class Intent(models.Model):
    """
    Класс представляет сообой сущность для сбора сообщений пользователя в один общий класс.
    Используется для обращения к базе данных
    """
    name = models.CharField(max_length=50)
    def inner_sentences(self):
        return ', '.join([item.text for item in self.inputsentence_set.all()])
    inner_sentences.short_description = 'орпропа'

    def __str__(self):
        # @input_sentences = ", ".join(self.inputsentence_set.all())
        return self.name  # "Response: [ sentences: {} ]".format(input_sentences)


class InputSentence(models.Model):
    """
    Класс представляет сообой сущность входных сообщений от пользователя.
    Используется для обращения к базе данных
    """
    text = models.CharField(max_length=150)
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    def __str__(self):
        # @input_sentences = ", ".join(self.inputsentence_set.all())
        return self.text  # "Response: [ sentences: {} ]".format(input_sentences)

class Response(models.Model):
    """
    Класс представляет сообой сущность ответов, которые бот отправляет пользователю.
    Используется для обращения к базе данных
    """
    text = models.CharField(max_length=1200)

    def __str__(self):
        # @input_sentences = ", ".join(self.inputsentence_set.all())
        return self.text
        # article = models.ForeignKey(Article)


# class IntentNode(models.Model):
#     nextNodes = models.PositiveIntegerField
#     flow = models.PositiveIntegerField
#     node = models.ForeignKey(Flow)


# class Flow (models.Model):

class Pair(models.Model):
    """
    Класс представляет сообой сущность для связи интентов и ответо между собой
    Используется для обращения к базе данных
    """
    responses = models.ManyToManyField(Response)
    intents = models.ManyToManyField(Intent)

    def inner_intents(self):
        return ', '.join([item.name for item in self.intents.all()])
    inner_intents.short_description = 'Intent'


    def inner_responses(self):
        return '\n '.join([item.text for item in self.responses.all()])
    inner_responses.short_description = 'Responses'


# class Article(models.Model):
#   articleName = models.CharField(max_length=150)
#  articleText = models.TextField()


class Users(models.Model):
    name_user = models.CharField(max_length=60)
    #  userState = models.ForeignKey(UserState)


class DisplayedMessages(models.Model):
    user = models.ForeignKey(Users)
    adv_or_train = models.ForeignKey(Response)
    date = models.DateField()


# class UserState(models.Model):
# flow
#  intent


class NotAnsweredMessage(models.Model):
    user = models.ForeignKey(Users)
    text = models.TextField()
    date = models.DateField()


class DialogHistory(models.Model):
    """
    Класс представляет сообой сущность для хранения сообщений полученных от пользователя и отправленных ботом.
    Используется для обращения к базе данных
    """
    chat_id = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    source = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

class IntentWords(models.Model):
    word = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class CorpusWords(models.Model):
    word = models.CharField(max_length=50)
    score = models.IntegerField()


