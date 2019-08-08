import datetime

from django.urls import reverse
from django.test import TestCase

from dateutil.parser import parse
from model_mommy import mommy


class TopTests(TestCase):

    def setUp(self):
        self.list_url = reverse('top-list')

    def test_can_rank_movies(self):
        movies = mommy.make('movie', _quantity=5)

        self._comment_movie(movies[4], 3)

        self._comment_movie(movies[3], 2)

        self._comment_movie(movies[1], 2)

        self._comment_movie(movies[2])

        resp = self.client.get(self.list_url, {'year__lte': datetime.MAXYEAR})

        self.assertListEqual(
            [
                {
                    'movie_id': movies[4].id,
                    'total_comments': 3,
                    'rank': 1,
                },
                {
                    'movie_id': movies[1].id,
                    'total_comments': 2,
                    'rank': 2,
                },
                {
                    'movie_id': movies[3].id,
                    'total_comments': 2,
                    'rank': 2,
                },
                {
                    'movie_id': movies[2].id,
                    'total_comments': 1,
                    'rank': 3,
                },
                {
                    'movie_id': movies[0].id,
                    'total_comments': 0,
                    'rank': 4,
                },
            ],
            resp.json()
        )

    def test_wont_include_movies_out_of_date_range(self):
        now_movie = mommy.make('movie', year=2019)
        future_movie = mommy.make('movie', year=2022)
        mommy.make('movie', year=1999)

        resp = self.client.get(self.list_url, {'year__gte': '2019'})

        self.assertEqual(2, len(resp.json()))
        self.assertListEqual(
            [now_movie.id, future_movie.id],
            [m['movie_id'] for m in resp.json()]
        )

    @staticmethod
    def _comment_movie(movie, n=1):
        mommy.make('comment', movie=movie, _quantity=n)
