from django.conf.urls import patterns, include, url
from django.contrib import admin

from propro.views import Home
from projects.views import ProjectEnvView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'), 
    url(r'^project_env/', ProjectEnvView.as_view(), name='project_env'),
)

# for development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
    ]
