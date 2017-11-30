# -*- coding: UTF-8 -*- 
from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.aesDecryptor import Prpcrypt


# from .aes_decryptor import Prpcrypt
# Create your models here.
#角色分两种：
#1.工程师：可以提交SQL上线单的工程师们，username字段为登录用户名，display字段为展示的中文名。
#2.审核人：可以审核并执行SQL上线单的管理者、高级工程师、系统管理员们。
class users(AbstractUser):
    display = models.CharField('显示的中文名', max_length=50)
    role = models.CharField('角色', max_length=20, choices=(('工程师','工程师'),('审核人','审核人')), default='工程师')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = u'用户配置'
        verbose_name_plural = u'用户配置'