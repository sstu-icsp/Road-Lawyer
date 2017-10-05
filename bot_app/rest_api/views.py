from rest_framework import viewsets

from dialog_manager.models import Response
from rest_api.serializers import ResponseSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
