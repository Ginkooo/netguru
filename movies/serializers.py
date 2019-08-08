from django.conf import settings

from rest_framework import serializers

from movies import models
from movies import omdb


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

    details = serializers.JSONField(required=False)

    def create(self, validated_data):
        details = omdb.OmdbApi().get(validated_data['title'])
        validated_data['details'] = details
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
