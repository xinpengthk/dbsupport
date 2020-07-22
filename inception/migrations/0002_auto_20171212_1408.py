# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-12 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import utils.AesCharField


class Migration(migrations.Migration):

    dependencies = [
        ('inception', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_config',
            name='cluster_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='集群名称'),
        ),
        migrations.AlterField(
            model_name='main_config',
            name='main_password',
            field=utils.AesCharField.AesCharField(max_length=300, verbose_name='登录主库的密码'),
        ),
        migrations.AlterField(
            model_name='sql_order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='sql_order',
            name='engineer',
            field=models.CharField(db_index=True, max_length=50, verbose_name='发起人'),
        ),
        migrations.AlterField(
            model_name='sql_order',
            name='workflow_name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='工单内容'),
        ),
    ]
