from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)


class Comment(models.Model):
    contents = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
