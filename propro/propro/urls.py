from django.conf.urls import patterns, include, url
from django.contrib import admin

from propro.views import Home

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),    
)
