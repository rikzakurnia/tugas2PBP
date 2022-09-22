from django.test import TestCase

# Create your tests here.
from multiprocessing.connection import Client
from urllib import response


# Create your tests here.

class MywatchlistTest(TestCase):
    def test_request_html(self):
        # c = Client()
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_request_xml(self):
        # c = Client()
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_request_json(self):
        # c = Client()
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)