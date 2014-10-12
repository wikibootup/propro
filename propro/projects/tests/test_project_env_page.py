from django.test import TestCase
from django.test.client import Client

from django.core.exceptions import ObjectDoesNotExist,ValidationError

from projects.views import ProjectEnvView
from projects.models import ProjectEnv, ProjectEnvManager

class ProjectEnvPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_team_name = "buildbuild_team"
        self.valid_project_name = "buildbuild_project"
        self.valid_lang = "python"
        self.valid_ver = "2.7.8"


        # need to find more eloquent way to test redirect url.
        self.TEST_SERVER_URL = "http://testserver"

    def test_get_project_env_page_request_should_return_200(self):
        response = self.client.get("/project_env/")
        self.assertEqual(response.status_code, 200)

    def test_post_project_env_page_with_valid_information_should_return_200(self):
        response = self.client.post("/project_env/", {
            "team_name" : self.valid_team_name,
            "project_name" : self.valid_project_name,
            "lang" : self.valid_lang,
            "ver" : self.valid_ver,
            })
        self.assertEqual(response.status_code, 200)

    def test_get_project_name_of_project_env_created_project_env_page(self):
        self.client.post("/project_env/", {
            "team_name" : self.valid_team_name,
            "project_name" : self.valid_project_name,
            "lang" : self.valid_lang,
            "ver" : self.valid_ver,
            })
        try:
            ProjectEnv.objects.get_project_name(self.valid_project_name)
        except:
            ObjectDoesNotExist("Check the get_project_name()")

