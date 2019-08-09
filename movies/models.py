import json

from django.db import models
from django.core import exceptions

from movies import utils


class Movie(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    year = models.IntegerField()

    def __repr__(self):
        return f'{self.title} from {self.year}'


class Comment(models.Model):
    contents = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'Comment about {self.movie.title}'
