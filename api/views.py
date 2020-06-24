from ghostpost.models import GhostModel
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import GhostModelSerializer


# Create your views here.
class GhostModelViewSet(viewsets.ModelViewSet):
    queryset = GhostModel.objects.all().order_by('-date')
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

    @action(detail=False)
    def boasts(self, request):
        list_boasts = self.queryset.filter(boast_or_roast='B')
        page = self.paginate_queryset(list_boasts)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list_boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        list_roasts = self.queryset.filter(boast_or_roast='R')
        page = self.paginate_queryset(list_roasts)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list_roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_rated(self, request):
        list_diff = GhostModel.objects.extra(
            select={'diff': 'up_vote - down_vote'}).order_by('-diff')
        page = self.paginate_queryset(list_diff)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list_diff, many=True)
        return Response(serializer.data)


# https://stackoverflow.com/questions/53982800/how-to-make-a-different-django-api-url-path
class GhostMagicView(generics.RetrieveDestroyAPIView):
    lookup_field = 'magic'
    permission_class = ()
    queryset = GhostModel.objects.all().order_by('-date')
    serializer_class = GhostModelSerializer
