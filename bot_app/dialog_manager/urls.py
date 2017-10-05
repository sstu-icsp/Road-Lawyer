from django.conf.urls import url

from dialog_manager import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
