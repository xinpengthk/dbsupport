#!/usr/bin/env python
#coding:utf-8

'''
Created on 2017-09-08

@Author: XinPeng
@Description: model
'''

from django.db import models
from utils import AesCharField


# from workflow.aes_decryptor import Prpcrypt
# Create your models here.
class host(models.Model):

    SERVICE_ENV_CHOICES = (
        ('QA', 'QA'),
        ('DEV', 'DEV'),
        ('PRD', 'PRD'),
        ('PRE_PRD', 'PRE_PRD'),
    )
    
    HOST_TYPE_CHOICES = (
        ('DB', 'DB'),
        ('WEB', 'WEB'),
        ('REDIS', 'REDIS'),
        ('NGINX', 'NGINX'),
    )
    
    HOST_ROLE_CHOICES = (
        ('GENERAL', 'GENERAL'),
        ('MASTER', 'MASTER'),
        ('SLAVE', 'SLAVE'),
    )

    businessName = models.CharField(db_column='business_name',
         max_length=32,
         null=False,
         blank=False,
         verbose_name='业务线名称',
         help_text='请输入业务线名称!'
    )

    serviceEnv = models.CharField(db_column='service_env',
        max_length=32,
        choices=SERVICE_ENV_CHOICES,
        default='PRD',
        verbose_name='服务器环境',
        help_text='请输入服务器环境!'
    )

    hostName = models.CharField(db_column='host_name',
        max_length=64,
        null=False,
        blank=False,
        verbose_name='主机名',
        help_text='请输入主机名!'
    )

    intranetIpAddr = models.GenericIPAddressField(db_column='intranet_ip_addr',
        null=False,
        blank=False,
        verbose_name='内网IP地址',
        help_text='请输入内网IP地址!'
    )

    publicIpAddr = models.GenericIPAddressField(db_column='public_ip_addr',
        verbose_name='公网IP地址',
        help_text='请输入公网IP地址!'
    )
    
    sshPort = models.CharField(db_column='ssh_port',
        max_length=8,
        null=False,
        blank=False,
        verbose_name='SSH端口号',
        help_text='请输入SSH端口号!'
    )

    hostType = models.CharField(db_column='host_type',
        max_length=32,
        choices=HOST_TYPE_CHOICES,
        default='WEB',
        verbose_name='服务器类型',
        help_text='请输入服务器类型!'
    )

    hostRole = models.CharField(db_column='host_role',
        max_length=32,
        choices=HOST_ROLE_CHOICES,
        default='GENERAL',
        verbose_name='服务器角色',
        help_text='请输入服务器角色!'
    )

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间',
    )

    def __str__(self):
        return '[%s-%s-%s]' %(self.businessName, self.hostName, self.intranetIpAddr)

    class Meta:
        db_table = 'cmdb_host' 
        verbose_name = u'服务器信息'
        verbose_name_plural = u'服务器信息'

class hostUser(models.Model):
    # 实现显示密码是密文，复制密码是明文功能
    host = models.ForeignKey(
        host,
        on_delete=models.DO_NOTHING,
        db_column='host',
        db_index=False,        
        verbose_name='主机',
        help_text='请选择主机！',
        
    )

    hostUser = models.CharField(db_column='host_user',
        max_length=64,
        null=False,
        blank=False,
        verbose_name='操作系统用户',
        help_text='请输入操作系统用户!'
    )

    hostPasswd = AesCharField.AesCharField(db_column='host_passwd',
        max_length=300,
        null=False,
        blank=False,
        verbose_name='操作系统密码'
    )

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间',
    )
    
    def __str__(self):
        return self.hostUser

#     def get(self, *args, **kwargs):
#         pc = Prpcrypt()
#         self.hostPasswd = pc.decrypt(self.hostPasswd)
#         super(hostUser, self).get(*args, **kwargs)
        
#     def save(self, *args, **kwargs):
#         pc = Prpcrypt() #初始化
#         self.hostPasswd = pc.encrypt(self.hostPasswd)
#         super(hostUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'cmdb_host_user' 
        verbose_name = u'机器用户密码'
        verbose_name_plural = u'机器用户密码'
        

class dbInstance(models.Model):
    INSTANCE_ROLE_CHOICES = (
        ('SINGLE', 'SINGLE'),
        ('MASTER', 'MASTER'),
        ('SLAVE', 'SLAVE'),
    )

    INSTANCE_TYPE_CHOICES = (
        ('MYSQL', 'MYSQL'),
        ('REDIS', 'REDIS'),
        ('ORACLE', 'ORACLE'),
        ('MONGO', 'MONGO'),
    )

    host = models.ForeignKey(
        host,
        on_delete=models.DO_NOTHING,
        db_column='host',
        db_index=False,        
        verbose_name='主机',
        help_text='请选择主机',
        
    )

    instanceName = models.CharField(db_column='instance_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='实例名',
        help_text='请输入实例名!'
    )

    instanceType = models.CharField(db_column='instance_type',
        max_length=32,
        choices=INSTANCE_TYPE_CHOICES,
        verbose_name='实例类型',
        help_text='请输入实例类型!'
    )
    
    portNum = models.IntegerField(db_column='port_num',
        null=False,
        blank=False,
        verbose_name='实例端口号',
        help_text='请输入实例端口号!',
    )
    
    instanceRole = models.CharField(db_column='instance_role',
        max_length=32,
        choices=INSTANCE_ROLE_CHOICES,
        default='MASTER',
        verbose_name='实例角色',
        help_text='请输入实例角色!'        
    )

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间!',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间!',
    )
    
    def __str__(self):
        return '[%s-%s-%s]' %(self.instanceName, self.instanceType, self.instanceRole)

    class Meta:
        db_table = 'cmdb_db_instance' 
        verbose_name = u'数据库实例'
        verbose_name_plural = u'数据库实例'    
    
class dbDatabase(models.Model):
    instance = models.ForeignKey(
        dbInstance,
        on_delete=models.DO_NOTHING,
        db_column='instance',
        db_index=False,        
        verbose_name='实例名',
        help_text='请选择实例！',
        
    )

    dbName = models.CharField(db_column='db_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='数据库名',
        help_text='请输入数据库名!'
    )

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间!',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间!',
    )

    def __str__(self):
        return self.dbName

    class Meta:
        db_table = 'cmdb_db_database' 
        verbose_name = u'数据库'
        verbose_name_plural = u'数据库' 

class dbPrivilege(models.Model):
    privName = models.CharField(db_column='priv_name',
        max_length=64,
        null=False,
        blank=False,
        verbose_name='权限名',
        help_text='请输入权限名!'
    )

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间!',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间!',
    )

    def __str__(self):
        return self.privName

    class Meta:
        db_table = 'cmdb_db_privs' 
        verbose_name = u'数据库权限'
        verbose_name_plural = u'数据库权限' 
    
class dbUser(models.Model):
    USER_TYPE_CHOICE = (
        ('WEB', 'WEB'),
        ('ADMIN', 'ADMIN'),
        ('SYS', 'SYS'),
        ('READ', 'READ'),
        ('BACKUP', 'BACKUP'),
        ('GENERAL', 'GENERAL'),
        ('MONITOR', 'MONITOR'),
        ('REPLICATION', 'REPLICATION'),
        ('INCEPTION', 'INCEPTION'),
        ('BIGDATA', 'BIGDATA'),
    )

    instance = models.ForeignKey(
        dbInstance,
        on_delete=models.DO_NOTHING,
        db_column='instance',
        db_index=False,        
        verbose_name='实例名',
        help_text='请选择实例！',
        
    )

    userName = models.CharField(db_column='user_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='用户名',
        help_text='请输入用户名!'
    )

    userPasswd = models.CharField(db_column='user_passwd',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='密码',
        help_text='请输入密码!'
    ) 

    userType = models.CharField(db_column='user_type',
        max_length=64,
        choices=USER_TYPE_CHOICE,
        verbose_name='用户类型',
        help_text='请输入用户类型!'
    )

    ipRange = models.CharField(db_column='ip_range',
        max_length=32,
        null=False,
        blank=False,
        verbose_name='IP范围',
        help_text='请输入IP范围!'
    ) 
    
    dbRange = models.ManyToManyField(dbDatabase)
    userPriv = models.ManyToManyField(dbPrivilege)

    createdTime = models.DateTimeField(db_column='created_time', 
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name='记录创建时间',
        help_text='该记录创建时间!',
    )
    
    updatedTime = models.DateTimeField(db_column='updated_time', 
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='记录最后更新时间',
        help_text='记录最后更新时间!',
    )

    def __str__(self):
        return '[%s-%s]' %(self.instance, self.userName)


#     def save(self, *args, **kwargs):
#         pc = Prpcrypt() #初始化
#         self.userPasswd = pc.encrypt(self.userPasswd)
#         super(dbUser, self).save(*args, **kwargs)
        

    class Meta:
        db_table = 'cmdb_db_user' 
        verbose_name = u'数据库用户'
        verbose_name_plural = u'数据库用户' 