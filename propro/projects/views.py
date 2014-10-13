from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from projects.forms import ProjectEnvForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.urlresolvers import reverse

from projects.models import ProjectEnv
from django.core.files import File

from django.http import HttpResponseRedirect
from django.contrib import messages

class ProjectEnvView(FormView):
    template_name = "projects/project_env.html"
    form_class = ProjectEnvForm


    def form_valid(self, form):
        team_name = self.request.POST["team_name"]
        project_name = self.request.POST["project_name"]
        lang = self.request.POST["lang"]
        ver = self.request.POST["ver"]
        docker_text = ""
        
        if "python" in lang:
            fileHandler = open(
                    "media/docker/python_Dockerfile",
                    'r'
                    )
        elif "ruby" in lang:
            fileHandler = open(
                    "media/docker/ruby_Dockerfile",
                    'r'
                    )

        docker_text = fileHandler.read()
        docker_text = docker_text.replace("<x.y>", ver[:3])
        docker_text = docker_text.replace("<x.y.z>", ver)

        project_env = ProjectEnv.objects.create_project_env( 
                team_name = team_name,
                project_name = project_name,
                properties = [lang, ver],
                docker_text = docker_text,
                )

        return HttpResponse(docker_text)


