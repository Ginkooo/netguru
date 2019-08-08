from django.conf import settings

import requests


class OmdbApi():

    def __init__(self):
        self.key = settings.OMDB_API_KEY

    def get(self, title):
        resp = requests.get(
            'http://www.omdbapi.com/',
            params={
                'apikey': self.key,
                't': str(title),
            }
        )
        return resp.json()
