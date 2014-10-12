from django.test import TestCase
from django.test.client import Client

from django.core.exceptions import ObjectDoesNotExist

from projects.views import ProjectEnvView

class RubyVerPageTest(TestCase):
    def setUp(self):
        self.client = Client()

        # need to find more eloquent way to test redirect url.
        self.TEST_SERVER_URL = "http://testserver"

    def test_get_project_env_page_request_should_return_200(self):
        response = self.client.get("/project_env/")
        self.assertEqual(response.status_code, 200)

