from rest_framework import serializers

from dialog_manager.models import Response


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Response
        fields = ('text',)
