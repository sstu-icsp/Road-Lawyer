from dialog_manager.models import DialogHistory


def save_user_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="User")


def save_bot_message(chat_id, text):
    save_message(chat_id=chat_id, text=text, source="Bot")


def save_message(chat_id, text, source):
    DialogHistory(chat_id=chat_id, text=text, source=source)
