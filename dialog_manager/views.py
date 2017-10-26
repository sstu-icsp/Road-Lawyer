from django.http import HttpResponse

from dialog_manager.models import Intent


def index(request):
    return HttpResponse(Intent.objects.all())
