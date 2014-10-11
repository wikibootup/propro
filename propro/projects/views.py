from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from projects.forms import PyVerForm
from django.core.exceptions import ValidationError
from django.contrib import messages

class PyVerView(FormView):
    template_name = "projects/pyver.html"
    form_class = PyVerForm

    def form_valid(self, form):
        select_pyver = self.request.POST["select_pyver"]
        print self.request.POST.keys()

        return HttpResponse(select_pyver)

