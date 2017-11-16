# -*- coding: UTF-8 -*- 

from django.conf.urls import url, include

from workflow import views


urlpatterns = [
    url(r'^$', views.allworkflow, name='allworkflow'),
    url(r'^index/$', views.allworkflow, name='allworkflow'),
    url(r'^login/$', views.login, name='login'),
]
