from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_catalog

class TestUrls(SimpleTestCase):
     def test_show_catalog_url(self):
        url = reverse('katalog:show_catalog')
        self.assertEqual(resolve(url).func, show_catalog)