from dialog_manager.models import Intent


class IntentService:
    @staticmethod
    def get_all_intent():
        return Intent.objects.all()
