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
    url(r'^getHostUserDetailInfo/$', views_ajax.getHostUserDetailInfo, name='getHostUserDetailInfo'),
    url(r'^getHostDetail/(?P<hostId>[0-9]+)/$', views.getHostDetail, name='getHostDetail'),
    url(r'^delHostUser/$', views_ajax.delHostUser, name='delHostUser'),
#     url(r'^getDbInstanceList/$', views.getDbInstanceList, name='getDbInstanceList'),
#     url(r'^getDbClusterList/$', views.getDbClusterList, name='getDbClusterList'),
#     url(r'^addDbClusterForm/$', views.addDbClusterForm, name='addDbClusterForm'),
#     url(r'^addChangeDbClusterInfo/$', views_ajax.addChangeDbClusterInfo, name='addChangeDbClusterInfo'),
#     url(r'^delDbCluster/$', views_ajax.delDbCluster, name='delDbCluster'),
#     url(r'^getDbClusterDetail/(?P<clusterId>[0-9]+)/$', views.getDbClusterDetail, name='getDbClusterDetail'),
    url(r'^getDbGroupList/$', views.getDbGroupList, name='getDbGroupList'),
    url(r'^getDbGroupDetailInfo/$', views_ajax.getDbGroupDetailInfo, name='getDbGroupDetailInfo'),
    url(r'^addDbGroupForm/$', views.addDbGroupForm, name='addDbGroupForm'),
    url(r'^addChangeDbGroupInfo/$', views_ajax.addChangeDbGroupInfo, name='addChangeDbGroupInfo'),
    url(r'^getInstanceDetail/(?P<groupId>[0-9]+)/$', views.getInstanceDetail, name='getInstanceDetail'),
    url(r'^addDbInstanceForm/(?P<groupId>[0-9]+)/$', views.addDbInstanceForm, name='addDbInstanceForm'),
    url(r'^addChangeDbInstanceInfo/$', views_ajax.addChangeDbInstanceInfo, name='addChangeDbInstanceInfo'),
    url(r'^getDbInstanceDetailInfo/$', views_ajax.getDbInstanceDetailInfo, name='getDbInstanceDetailInfo'),
    url(r'^changDbInstanceForm/$', views.changDbInstanceForm, name='changDbInstanceForm'),
    url(r'^delDbInstance/$', views_ajax.delDbInstance, name='delDbInstance'),

]
