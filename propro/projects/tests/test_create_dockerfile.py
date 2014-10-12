from django.test import TestCase
from django.test.client import Client

from django.core.exceptions import ObjectDoesNotExist

from projects.views import ProjectEnvView

from django.core.files import File

class CreateDockerfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_team_name = "buildbuild_team"
        self.valid_project_name = "buildbuild_project"
        self.valid_lang = "python"
        self.valid_ver = "2.7.8"

        # need to find more eloquent way to test redirect url.
        self.TEST_SERVER_URL = "http://testserver"

    def test_open_file(self):
        try:
            fileHandler = open(
                    "media/docker/python_Dockerfile",
                    'r'
                    )
        except:
            self.fail("file open failed")

    def test_string_replace(self):
        docker_text = ""
        try:
            fileHandler = open(
                    "media/docker/python_Dockerfile",
                    'r'
                    )
            docker_text = fileHandler.read()
            docker_text = docker_text.replace("<x.y>", self.valid_ver[:3])
            docker_text = docker_text.replace("<x.y.z>",self.valid_ver)
            print docker_text 
        except:
            self.fail("file open failed")

    def test_post_project_env_page_with_valid_information_should_return_200(self):
        response = self.client.post("/project_env/", {
            "team_name" : self.valid_team_name,
            "project_name" : self.valid_project_name,
            "lang" : self.valid_lang,
            "ver" : self.valid_ver,
            })
        self.assertEqual(response.status_code, 200)


