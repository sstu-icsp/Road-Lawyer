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

def simple_classifier(text):
    for pair in Pair.objects.all():
        intent_tmp = pair.intent.inputsentence_set.all()
        for sentences in intent_tmp:
            if (sentences.text == text):
                return pair.list_response.all()

def NB_classifier():

    masX = []
    masY = []

    for intent in models.Intent.objects.all():
        tmp = intent.inputsentence_set.all()
        for sentences in tmp:
            masY.append(intent.name)
            masX.append(sentences.intent.name)

    X = vector.fit_transform(np.array(masX))
    Y = np.array(masY)

    clf.fit(X, Y)


def get_response(chat_id, text):
    intent_name = clf.predict(vector.transform(text))
    pairs = models.Pair.objects.all()
    flag = False
    for pair in pairs:
        if(intent_name == pair.intent.name):
            flag == True
            return pair.list_response.all()
    if(flag == False):
        from datetime import datetime
        date = datetime.now()
        models.NotAnsweredMessage(chat_id, text, date)



