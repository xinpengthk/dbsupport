# -*- coding: UTF-8 -*- 

from django.conf.urls import url

from inception import views, views_ajax


urlpatterns = [
#     url(r'^$', views.allworkflow, name='allworkflow'),
#     url(r'^index/$', views.allworkflow, name='allworkflow'),
#     url(r'^$', views.allworkflow, name='allworkflow'),
    url(r'^$', views.getWorkOrderList, name='getWorkOrderList'),    
    url(r'^submitsql/$', views.submitSql, name='submitSql'),
    url(r'editsql/$', views.submitSql, name='editsql'),
#     url(r'^allworkflow/$', views.allworkflow, name='allworkflow'),
    url(r'^allworkflow/$', views.getWorkOrderList, name='getWorkOrderList'),
    url(r'^autoreview/$', views.autoreview, name='autoreview'),
    url(r'^detail/(?P<workflowId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^execute/$', views.execute, name='execute'),
    url(r'^cancel/$', views.cancel, name='cancel'),
    url(r'^rollback/$', views.rollback, name='rollback'),
    url(r'^dbaprinciples/$', views.dbaprinciples, name='dbaprinciples'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^simplecheck/$', views_ajax.simplecheck, name='simplecheck'),
    url(r'^getMonthCharts/$', views_ajax.getMonthCharts, name='getMonthCharts'),
    url(r'^getPersonCharts/$', views_ajax.getPersonCharts, name='getPersonCharts'),
    url(r'^getOscPercent/$', views_ajax.getOscPercent, name='getOscPercent'),
    url(r'^getWorkflowStatus/$', views_ajax.getWorkflowStatus, name='getWorkflowStatus'),
    url(r'^stopOscProgress/$', views_ajax.stopOscProgress, name='stopOscProgress'),
    url(r'^masterConfigList/$', views.masterConfigList, name='masterConfigList'),
    url(r'^addMasterConfigForm/$', views.addMasterConfigForm, name='addMasterConfigForm'),
    url(r'^addMasterConfig/$', views_ajax.addMasterConfig, name='addMasterConfig'),
    url(r'^delMasterConfig/$', views_ajax.delMasterConfig, name='delMasterConfig'),
    url(r'^getSqlWorkOrderList/$', views.getSqlWorkOrderList, name='getSqlWorkOrderList'),
    url(r'^delsqlOrder/$', views_ajax.delsqlOrder, name='delsqlOrder'),
    url(r'^getSqlWorkOrderDetail/(?P<sqlOrderId>[0-9]+)/$', views.getSqlWorkOrderDetail, name='getSqlWorkOrderDetail'),
#     url(r'^sqlWorkOrderSearch/$', views.sqlWorkOrderSearch, name='sqlWorkOrderSearch'),
    
]
