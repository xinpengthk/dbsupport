#!/usr/bin/env python
#coding:utf-8

'''
Created on 2017-09-08

@Author: XinPeng
@Description: model
'''

from django.contrib import admin

# Register your models here.
from cmdb.models import host, hostUser, dbInstance, dbDatabase, dbPrivilege, dbUser

class hostAdmin(admin.ModelAdmin):
    list_display = ('id', 'businessName', 'serviceEnv', 'hostName', 'intranetIpAddr', 'publicIpAddr', 'sshPort', 'hostType', 'hostRole', 'createdTime', 'updatedTime')
    search_fields = ['id', 'businessName', 'serviceEnv', 'hostName', 'intranetIpAddr', 'publicIpAddr', 'sshPort', 'hostType', 'hostRole']

class hostUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'hostUser', 'hostPasswd', 'createdTime', 'updatedTime')
    search_fields = ['id', 'host__businessName', 'host__hostName', 'host__intranetIpAddr', 'hostUser', 'hostPasswd', 'createdTime', 'updatedTime']
    
class dbInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'instanceName', 'instanceType', 'portNum', 'instanceRole', 'createdTime', 'updatedTime')
    search_fields = ['id', 'host__businessName', 'host__hostName', 'host__intranetIpAddr', 'instanceName', 'instanceType', 'portNum', 'instanceRole', 'createdTime', 'updatedTime']
    
class dbDatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'instance', 'dbName', 'createdTime', 'updatedTime')
    search_fields = ['id', 'instance__instanceName', 'instance__instanceType', 'instance__instanceRole', 'dbName', 'createdTime', 'updatedTime']

class dbPrivilegeAdmin(admin.ModelAdmin):
    list_display = ('id', 'privName', 'createdTime', 'updatedTime')
    search_fields = ['id', 'privName', 'createdTime', 'updatedTime']

class dbUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'instance', 'userName', 'userPasswd', 'userType', 'ipRange', 'createdTime', 'updatedTime')
    search_fields = ['id', 'instance__instanceName', 'instance__instanceType', 'instance__instanceRole', 'userName', 'userPasswd', 'userType', 'ipRange', 'createdTime', 'updatedTime']
    
    
admin.site.register(host, hostAdmin)
admin.site.register(hostUser, hostUserAdmin)
admin.site.register(dbInstance, dbInstanceAdmin)
admin.site.register(dbDatabase, dbDatabaseAdmin)
admin.site.register(dbPrivilege, dbPrivilegeAdmin)
admin.site.register(dbUser, dbUserAdmin)
