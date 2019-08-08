from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from movies import models, serializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filterset_fields = '__all__'
