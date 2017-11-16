#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Created on 2017年11月15日

@author: xinpeng
'''

from django.core import validators, checks
from django.db.models.fields import Field
from django.utils import six
from django.utils.encoding import smart_text
from utils.aesDecryptor import Prpcrypt


class AesCharField(Field):
    description = "just a AES Char filed"

    def __init__(self, *args, **kwargs):
        super(AesCharField, self).__init__(*args, **kwargs)
        self.validators.append(validators.MaxLengthValidator(self.max_length))

    def check(self, **kwargs):
        errors = super(AesCharField, self).check(**kwargs)
        errors.extend(self._check_max_length_attribute(**kwargs))
        return errors

    def _check_max_length_attribute(self, **kwargs):
        if self.max_length is None:
            return [
                checks.Error(
                    "AesCharFields must define a 'max_length' attribute.",
                    obj=self,
                    id='fields.E120',
                )
            ]
        elif not isinstance(self.max_length, six.integer_types) or self.max_length <= 0:
            return [
                checks.Error(
                    "'max_length' must be a positive integer.",
                    obj=self,
                    id='fields.E121',
                )
            ]
        else:
            return []

    def to_python(self, value):
        if isinstance(value, six.string_types) or value is None:
            return value
        return smart_text(value)

    def get_internal_type(self):
        return "CharField"

    # 读取数据库的时候调用这个方法
    def from_db_value(self, value, expression, conn, context):
        if value is None:
            return value
        pc = Prpcrypt() 
        return pc.decrypt(value)

    # 保存数据库的时候调用这个方法
    def get_prep_value(self, value):
        if value is None:
            return value
        pc = Prpcrypt()
        value = pc.encrypt(super(AesCharField, self).get_prep_value(value))
        return self.to_python(value)

    def formfield(self, **kwargs):
        # Passing max_length to forms.AesCharField means that the value's length
        # will be validated twice. This is considered acceptable since we want
        # the value in the form field (to pass into widget for example).
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super(AesCharField, self).formfield(**defaults)
