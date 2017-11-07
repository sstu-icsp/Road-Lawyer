from dialog_manager.models import DialogHistory, Intent, Pair

def save_user_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="User")


def save_bot_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="Bot")


def save_message(chat_id, text, source):
    DialogHistory(chat_id=chat_id, text=text, source=source)

def simple_classifier(chat_id, text):
    for pair in Pair.objects.all():
        intent_tmp = pair.intent.inputsentence_set.all()
        for sentences in intent_tmp:
            if (sentences.text == text):
                return pair.list_response.all()




