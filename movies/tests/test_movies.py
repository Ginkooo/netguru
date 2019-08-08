import json
from unittest import mock

from django.test import TestCase
from django.urls import reverse

from dateutil.parser import parse
from model_mommy import mommy


class MovieTests(TestCase):

    def setUp(self):

        self.list_url = reverse('movie-list')

        self.omdb_sample_data = {
            'Title': 'Harry Potter',
            'Year': '2001',
        }

        resp_mock = mock.MagicMock()

        def json():
            return self.omdb_sample_data

        resp_mock.json = json
        self.omdb_mock = mock.patch(
            'requests.get',
            return_value=resp_mock,
        ).start()

    def tearDown(self):
        mock.patch.stopall()

    def test_can_add_movie_only_with_title(self):
        expected_title = 'Harry Potter'
        resp = self.client.post(
            self.list_url,
            {'title': expected_title},
        )

        self.assertEqual(201, resp.status_code)
        self.assertEqual(expected_title, resp.json()['title'])

        resp = self.client.post(
            self.list_url,
            {},
        )

        self.assertEqual(400, resp.status_code)


    def test_will_include_data_from_ombd_on_save(self):
        title = 'Harry Potter'
        resp = self.client.post(self.list_url, {'title': title})

        self.assertDictEqual(
            self.omdb_sample_data,
            resp.json()['details']
        )

    def test_can_list_movies(self):
        movies = mommy.make('movie', _quantity=2)

        resp = self.client.get(self.list_url)

        self.assertEqual(2, len(resp.json()))

        for res_movie, exp_movie in zip(resp.json(), movies):
            self.assertEqual(exp_movie.title, res_movie['title'])
            self.assertIn('details', res_movie)

    def test_can_order_movies_by_title(self):
        mommy.make('movie', title='b')
        mommy.make('movie', title='a')

        resp = self.client.get(self.list_url, {'ordering': 'title'})

        self.assertListEqual('a b'.split(), [m['title'] for m in resp.json()])