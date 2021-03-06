#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Created on 2017年12月12日

@Author: Xinpeng
@Description: 用来处理json is not JSON serializable。
'''
import json  
import datetime  
  
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, datetime.date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 