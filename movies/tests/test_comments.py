from django.urls import reverse
from django.test import TestCase

from model_mommy import mommy


class CommentTests(TestCase):

    def test_can_comment_a_movie(self):
        url = reverse('comment-list')
        movie = mommy.make('movie')

        resp = self.client.post(
            url,
            {
                'contents': 'Nice film',
                'movie': movie.id,
            },
        )

        self.assertEqual(201, resp.status_code)
        self.assertEqual(movie.id, resp.json()['movie'])
        self.assertEqual('Nice film', resp.json()['contents'])
