import json
from unittest import mock

from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy


class MovieTests(TestCase):

    def setUp(self):
        self.omdb_sample_data = {
            'Title': 'Harry Potter',
            'Year': '2001',
        }

        omdb_mock = mock.MagicMock()
        omdb_mock.get.return_value = self.omdb_sample_data
        self.omdb_mock = mock.patch(
            'movies.omdb.OmdbApi',
            return_value=omdb_mock,
        ).start()

    def tearDown(self):
        mock.patch.stopall()

    def test_can_add_movie_only_with_title(self):
        url = reverse('movie-list')

        expected_title = 'Harry Potter'
        resp = self.client.post(
            url,
            {'title': expected_title},
        )

        self.assertEqual(201, resp.status_code)
        self.assertEqual(expected_title, resp.json()['title'])

        resp = self.client.post(
            url,
            {},
        )

        self.assertEqual(400, resp.status_code)

    def test_will_include_data_from_ombd_on_save(self):
        url = reverse('movie-list')

        title = 'Harry Potter'
        resp = self.client.post(url, {'title': title})

        self.assertDictEqual(
            self.omdb_sample_data,
            resp.json()['details']
        )

    def test_can_list_movies(self):
        movies = mommy.make('movie', _quantity=2)

        url = reverse('movie-list')

        resp = self.client.get(url)

        self.assertEqual(2, len(resp.json()))

        for res_movie, exp_movie in zip(resp.json(), movies):
            self.assertEqual(exp_movie.title, res_movie['title'])
            self.assertIn('details', res_movie)
