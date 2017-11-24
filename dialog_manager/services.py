from dialog_manager.models import DialogHistory, Intent, Pair
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import *
from dialog_manager import models

clf = BernoulliNB()
vector = TfidfVectorizer()


def save_user_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="User")


def save_bot_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="Bot")


def save_message(chat_id, text, source):
    DialogHistory(chat_id=chat_id, text=text, source=source)


def simple_classifier(chat_id, text):
    for pair in Pair.objects.all():
        for intent in pair.intents.all():
            for sentence in intent.inputsentence_set.all():
                if sentence.text.lower() == text.lower():
                    return pair.responses.all()


def nb_classifier():
    mas_x = []
    mas_y = []

    for intent in models.Intent.objects.all():
        tmp = intent.inputsentence_set.all()
        for sentences in tmp:
            mas_y.append(intent.name)
            mas_x.append(sentences.intent.name)

    x = vector.fit_transform(np.array(mas_x))
    y = np.array(mas_y)

    clf.fit(x, y)


def get_response(chat_id, text):
    intent_name = clf.predict(vector.transform(text))
    pairs = models.Pair.objects.all()
    flag = False
    for pair in pairs:
        if (intent_name == pair.intent.name):
            flag == True
            return pair.list_response.all()
    if (flag == False):
        from datetime import datetime
        date = datetime.now()
        models.NotAnsweredMessage(chat_id, text, date)
