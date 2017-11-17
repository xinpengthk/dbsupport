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


class BaseAdmin(object):
    """自定义admin类"""
    choice_fields = []
    fk_fields = []
    dynamic_fk = None
    dynamic_list_display = []
    dynamic_choice_fields = []
    m2m_fields = []
    
class hostUserInline(admin.TabularInline):
    model = hostUser
    readonly_fields = ['createdTime', 'updatedTime']
    list_display = ('id', 'host', 'hostUser', 'hostPasswd', 'createdTime', 'updatedTime')
    search_fields = ['id', 'host__businessName', 'host__hostName', 'host__intranetIpAddr', 'hostUser', 'hostPasswd', 'createdTime', 'updatedTime'] 

class hostAdmin(admin.ModelAdmin):
    readonly_fields = ['createdTime', 'updatedTime']
    inlines = [hostUserInline]
    list_per_page = 15
    list_display = ('id', 'businessName', 'serviceEnv', 'hostName', 'intranetIpAddr', 'publicIpAddr', 'sshPort', 'hostType', 'hostRole', 'createdTime', 'updatedTime')
    search_fields = ['id', 'businessName', 'serviceEnv', 'hostName', 'intranetIpAddr', 'publicIpAddr', 'sshPort', 'hostType', 'hostRole']
    ordering = ('id',)

class dbUserAdmin(admin.ModelAdmin):
    model = dbUser
    list_per_page = 15
    readonly_fields = ['createdTime', 'updatedTime']
    list_display = ('id', 'instance', 'userName', 'userPasswd', 'userType', 'ipRange', 'createdTime', 'updatedTime')
    search_fields = ['id', 'instance__instanceName', 'instance__instanceType', 'instance__instanceRole', 'userName', 'userPasswd', 'userType', 'ipRange', 'createdTime', 'updatedTime']
    ordering = ('id',)

class dbDatabaseInline(admin.TabularInline):
    model = dbDatabase
    readonly_fields = ['createdTime', 'updatedTime']
    list_display = ('id', 'instance', 'dbName', 'createdTime', 'updatedTime')
    search_fields = ['id', 'instance__instanceName', 'instance__instanceType', 'instance__instanceRole', 'dbName', 'createdTime', 'updatedTime']

class dbInstanceAdmin(admin.ModelAdmin):
    model = dbInstance
    list_per_page = 15
    inlines = [dbDatabaseInline]
    readonly_fields = ['createdTime', 'updatedTime']
    list_display = ('id', 'host', 'instanceName', 'instanceType', 'portNum', 'instanceRole', 'createdTime', 'updatedTime')
    search_fields = ['id', 'host__businessName', 'host__hostName', 'host__intranetIpAddr', 'instanceName', 'instanceType', 'portNum', 'instanceRole', 'createdTime', 'updatedTime']
    ordering = ('id',)
    
# class dbPrivilegeAdmin(admin.ModelAdmin):
#     model = dbPrivilege
#     list_per_page = 15
#     readonly_fields = ['createdTime', 'updatedTime']
#     list_display = ('id', 'privName', 'privDesc', 'createdTime', 'updatedTime')
#     search_fields = ['id', 'privName', 'privDesc', 'createdTime', 'updatedTime']


    
admin.site.register(host, hostAdmin)
# admin.site.register(hostUser)
admin.site.register(dbInstance, dbInstanceAdmin)
# admin.site.register(dbDatabase, dbDatabaseAdmin)
# admin.site.register(dbPrivilege, dbPrivilegeAdmin)
admin.site.register(dbUser, dbUserAdmin)


# admin.site.register(host)
# admin.site.register(hostUser)
# admin.site.register(dbInstance)
# admin.site.register(dbDatabase)
# admin.site.register(dbPrivilege)
# admin.site.register(dbUser)
