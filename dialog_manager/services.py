from dialog_manager.models import *
import nltk


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
def train():
    training_data = []
    for intent in Intent.objects.all():
        for sentence in intent.inputsentence_set.all():
            training_data.append({"intent":intent.name, "sentence":sentence.text})

    corpus_words = {}
    intent_words = {}

    intents = list(set([a['intent'] for a in training_data]))
    for c in intents:
        intent_words[c] = []

    for data in training_data:
        for word in nltk.word_tokenize(data['sentence']):
            if word not in ["?", "'s"]:
                stemmed_word = word.lower()
                if stemmed_word not in corpus_words:
                    corpus_words[stemmed_word] = 1
                else:
                    corpus_words[stemmed_word] += 1
                intent_words[data['intent']].extend([stemmed_word])

    IntentWords.objects.all().delete()
    CorpusWords.objects.all().delete()
    for key, value in intent_words.items():
        for word in value:
            IntentWords(word = word, name = key)

    for key, value in corpus_words.items():
        CorpusWords(word=key, score=value)


def calculate_class_score(sentence, intent_name):
    score = 0
    for word in nltk.word_tokenize(sentence):
        if word.lower() in IntentWords.objects.filter(name = intent_name):
            score += (1 / CorpusWords.objects.filter(word = word.lower()))
    return score

def classify(sentence):
    high_intent = None
    high_score = 0
    for intent_words in IntentWords.objects.all():
        score = calculate_class_score(sentence, intent_words.name)
        if score > high_score:
            high_intent = intent_words.name
            high_score = score

    return high_intent, high_score

def convert_to_array():
    corpus_words = {}
    intent_words = {}

    # Если я ничего не напутал то вот так вроде правильно

    for c in IntentWords.objects.all():
        intent_words[c.name.extend(c.word)]

    for c in CorpusWords.objects.all():
        corpus_words[c.word] = c.score
