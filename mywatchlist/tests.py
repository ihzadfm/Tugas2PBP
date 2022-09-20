from django.test import TestCase

# Create your tests here.
class TestUrl(TestCase):
    def test_url_html_exists(self):
        response = Client().get('https://tugas2pbpihza.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_url_xml_exists(self):
        response = Client().get('https://tugas2pbpihza.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url_json_exists(self):
        response = Client().get('https://tugas2pbpihza.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)