from django.test import TestCase
from django.test import Client

# Create your tests here.
class TestMyWatchListUrl(TestCase):
    def testmywatchlisturl_html_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def testmywatchlisturl_xml_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def testmywatchlisturl_json_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)