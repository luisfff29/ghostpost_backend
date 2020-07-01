from ghostpost.models import GhostModel
from rest_framework import serializers


class GhostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GhostModel
        fields = ['url', 'text', 'boast_or_roast',
                  'up_vote', 'down_vote', 'date', 'total_votes', 'magic']
