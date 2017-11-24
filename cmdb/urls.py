# -*- coding: UTF-8 -*- 

from django.conf.urls import url, include

from cmdb import views


urlpatterns = [
    url(r'^$', views.getHostInfo, name='getHostInfo'),
    url(r'^gethostinfo/$', views.getHostInfo, name='getHostInfo'),
]
