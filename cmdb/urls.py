# -*- coding: UTF-8 -*- 

from django.conf.urls import url, include

from cmdb import views, views_ajax


urlpatterns = [
    url(r'^$', views.getHostList, name='getHostList'),
    url(r'^getHostList/$', views.getHostList, name='getHostList'),
    url(r'^addHostForm/$', views.addHostForm, name='addHostForm'),
    url(r'^addChangeHostInfo/$', views_ajax.addChangeHostInfo, name='addChangeHostInfo'),
    url(r'^getHostDetailInfo/$', views_ajax.getHostDetailInfo, name='getHostDetailInfo'),
    url(r'^delHost/$', views_ajax.delHost, name='delHost'),
    url(r'^addHostUserForm/$', views.addHostUserForm, name='addHostUserForm'),
    url(r'^addChangeHostUserInfo/$', views_ajax.addChangeHostUserInfo, name='addChangeHostUserInfo'),
    url(r'^getHostDetail/(?P<hostId>[0-9]+)/$', views.getHostDetail, name='getHostDetail'),
    url(r'^delHostUser/$', views_ajax.delHostUser, name='delHostUser'),
    
]
