# -*- coding: UTF-8 -*- 

from django.conf.urls import url

from user import views, views_ajax


urlpatterns = [
    url(r'^$', views.loginSuccessful, name='loginSuccessful'),
    url(r'^index/$', views.loginSuccessful, name='loginSuccessful'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^authenticate/$', views_ajax.authenticateEntry, name='authenticate'),
    url(r'^changepasswd/$', views_ajax.changePasswd, name='changePasswd'),
    url(r'^changepasswdpost/$', views.changePasswd, name='changePasswdPost'),
    url(r'^getUserList/$', views.getUserList, name='getUserList'),
    url(r'^addUserForm/$', views.addUser, name='addUserForm'),
    url(r'^addChangeUserInfo/$', views_ajax.addChangeUserInfo, name='addChangeUserInfo'),
    url(r'^delUser/$', views_ajax.delUser, name='delUser'),
    url(r'^resetUserPasswd/$', views_ajax.resetUserPasswd, name='resetUserPasswd'),

]
