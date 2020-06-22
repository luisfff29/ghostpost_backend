from ghostpost.models import GhostModel
from rest_framework import serializers


class GhostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GhostModel
        fields = '__all__'
