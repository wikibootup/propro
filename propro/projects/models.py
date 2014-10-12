from django.db import models
from jsonfield import JSONField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError

class ProjectEnvManager(models.Manager):
    def create_project_env(self, team_name, project_name, properties, **kwargs):
        self.validate_project_name(project_name)
        project_env = self.model(
                team_name = team_name,
                project_name = project_name,
                properties = properties,
                )

        if "docker_text" in kwargs:
            project_env.docker_text = kwargs['docker_text']
            
        project_env.save(using = self._db)
        return project_env

    def validate_project_name(self, project_name):
        try:
            ProjectEnv.objects.get(project_name=project_name)
        except:
            return True
        else:
            raise ValidationError("The project name already exists")

    def get_project_env(self, project_name):
        try:
            project_env = ProjectEnv.objects.get(project_name=project_name)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(project_name + "Does not exist")
        return project_env

    def delete_project_env(self, project_name):
        project_env = ProjectEnv.objects.get_project_env(project_env)
        project_env.deactivate()
        project_env.save(using = self._db)

class ProjectEnv(models.Model):
    team_name = models.CharField(default="none", max_length=20, unique=True)
    project_name = models.CharField(default="none", max_length=20, unique=True)
    properties = JSONField()
    docker_text = models.TextField(default="none")
    objects = ProjectEnvManager() # The default manager.

