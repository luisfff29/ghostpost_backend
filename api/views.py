from ghostpost.models import GhostModel
from rest_framework import viewsets
from api.serializers import GhostModelSerializer


# Create your views here.
class GhostModelViewSet(viewsets.ModelViewSet):
    queryset = GhostModel.objects.all()
    serializer_class = GhostModelSerializer
