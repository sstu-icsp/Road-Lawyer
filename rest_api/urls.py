from django.conf.urls import url

from rest_api.views import get_answer

# Список URLs апи
urlpatterns = [
    url(r'^answer/$', get_answer)
]