from django.http import HttpResponse

from dialog_manager.serivices import get_all_intent


def index(request):
    response = get_all_intent()
    return HttpResponse(response)
