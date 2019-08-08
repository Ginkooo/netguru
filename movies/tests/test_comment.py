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

    def test_can_list_comments(self):
        url = reverse('comment-list')
        comments = mommy.make('comment', _quantity=2)

        resp = self.client.get(url)

        self.assertEqual(2, len(resp.json()))
        for exp_comment, res_comment in zip(comments, resp.json()):
            self.assertEqual(exp_comment.contents, res_comment['contents'])


    def test_can_filter_comments_by_movie_id(self):
        url = reverse('comment-list')

        movie = mommy.make('movie')
        comment = mommy.make('comment', movie=movie)
        mommy.make('comment')

        resp = self.client.get(url, {'movie': movie.id})

        self.assertEqual(1, len(resp.json()))
        self.assertEqual(comment.id, resp.json()[0]['id'])
