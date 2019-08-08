from collections import namedtuple

from django.db.models import Count

from rest_framework import viewsets, exceptions, filters
from rest_framework.response import Response

from movies import models, serializers


class TopViewSet(viewsets.ViewSet):

    def list(self, request):
        movies = models.Movie.objects\
            .filter(**request.query_params.dict())\
            .annotate(
            total_comments=Count('comment'),
        ).order_by('-total_comments')

        return Response([
            {
                'movie_id': top.movie.id,
                'total_comments': top.movie.total_comments,
                'rank': top.rank
            }
            for top in self._make_top_list(movies)
        ])

    @staticmethod
    def _make_top_list(movies):
        TopList = namedtuple('TopList', 'rank movie')

        ret = []
        prev_top = None
        for movie in movies:
            if not prev_top:
                top = TopList(rank=1, movie=movie)
                ret.append(top)
                prev_top = top
            elif movie.total_comments == prev_top.movie.total_comments:
                top = TopList(rank=prev_top.rank, movie=movie)
                ret.append(top)
                prev_top = top
            else:
                top = TopList(rank=prev_top.rank+1, movie=movie)
                ret.append(top)
                prev_top = top

        return ret
