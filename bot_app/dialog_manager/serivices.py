from dialog_manager.models import Intent


def get_all_intent():
    return Intent.objects.all()