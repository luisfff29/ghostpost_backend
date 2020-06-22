from ghostpost.models import GhostModel
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import GhostModelSerializer


# Create your views here.
class GhostModelViewSet(viewsets.ModelViewSet):
    queryset = GhostModel.objects.all()
    serializer_class = GhostModelSerializer

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_vote += 1
        post.save()
        return Response({'status': 'up vote set'})

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_vote += 1
        post.save()
        return Response({'status': 'down vote set'})
