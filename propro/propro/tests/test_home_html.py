from django.test import TestCase
from django.test.client import Client

from django.core.exceptions import ObjectDoesNotExist

from propro.views import Home

class Home_Html_Test(TestCase):
    def setUp(self):
        self.client = Client()

        # need to find more eloquent way to test redirect url.
        self.TEST_SERVER_URL = "http://testserver"

    def test_get_home_main_page_request_should_return_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


