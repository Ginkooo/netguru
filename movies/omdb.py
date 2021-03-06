from django.conf import settings
from rest_framework import exceptions

import requests

from movies import utils


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
        data = resp.json()
        if not utils.is_truthy(data.get('Response')):
            raise exceptions.APIException('Sorry, there is no such film in OMDb database')
        return data
