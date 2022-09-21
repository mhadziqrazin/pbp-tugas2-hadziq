from django.test import Client, TestCase, RequestFactory
from django.urls import reverse, resolve
from mywatchlist.views import show_watchlist, show_watchlist_json, show_watchlist_xml

# Create your tests here.
class TestUrls(TestCase):
    def tets_mywatchlist_http_response_html(self):
        c = Client()
        response = c.get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)
    
    def tets_mywatchlist_http_response_xml(self):
        c = Client()
        response = c.get('/mywatchlist/xml')
        self.assertEqual(response.status_code, 200)
    
    def tets_mywatchlist_http_response_json(self):
        c = Client()
        response = c.get('/mywatchlist/json')
        self.assertEqual(response.status_code, 200)