from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class Lang(TemplateView):
    template_name = "lang.html"


