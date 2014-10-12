from django.test import TestCase
from projects.models import ProjectEnv
from django.core.exceptions import ObjectDoesNotExist,ValidationError

class TestUserManager(TestCase):
    def setUp(self):
        self.projectenv = ProjectEnv()
        self.valid_team_name = "buildbuild_team"
        self.valid_project_name = "buildbuild_project"
        self.valid_properties = ["python", "2.7.8"]

        self.valid_team_name_2 = "buildbuild_team_2"
        self.valid_project_name_2 = "buildbuild_project_2"
        
    def test_projectenv_manager_could_create_projectenv(self):
        try:
            project_env = ProjectEnv.objects.create_project_env(
                    self.valid_team_name,
                    self.valid_project_name,
                    self.valid_properties,
            )
        except:
            self.fail("ProjectEnvManager could create ProjectEnv")

    def test_project_name_must_be_unique(self):
        try:
            project_env = ProjectEnv.objects.create_project_env(
                    self.valid_team_name,
                    self.valid_project_name,
                    self.valid_properties,
            )
            project_env = ProjectEnv.objects.create_project_env(
                    self.valid_team_name_2,
                    self.valid_project_name,
                    self.valid_properties,
            )
        except:
            pass
        else:
            self.fail("Check the unique code of the project")

      
