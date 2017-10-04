from django.http import HttpResponse

from dialog_manager.models import Intent
from dialog_manager.services.intent_service import IntentService


def index(request):
    response = IntentService.get_all_intent()[0].__str__()
    return HttpResponse(response)
