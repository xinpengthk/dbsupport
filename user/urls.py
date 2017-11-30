# -*- coding: UTF-8 -*- 

from django.conf.urls import url, include

from user import views, views_ajax


urlpatterns = [
    url(r'^$', views.loginSuccessful, name='loginSuccessful'),
    url(r'^index/$', views.loginSuccessful, name='loginSuccessful'),    
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^authenticate/$', views_ajax.authenticateEntry, name='authenticate'),
    url(r'^changepasswd/$', views_ajax.changePasswd, name='changePasswd'),
]
