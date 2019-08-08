import json

from django.db import models
from django.core import exceptions

from movies import utils


class Movie(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(default=set)
    year = models.IntegerField()


class Comment(models.Model):
    contents = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
