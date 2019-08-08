from rest_framework import viewsets

from movies import models, serializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filterset_fields = ['movie']
