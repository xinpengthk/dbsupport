#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Created on 2017年12月14日

@author: xinpeng
@
'''

import logging
import logging.config
import os.path
import yaml


def getLogger():
    logConfigFile = r"dbsupport/dbsupport/logConfig.yaml"
    print(logConfigFile)
    print(os.path.abspath(logConfigFile))
    logging.config.dictConfig(yaml.load(open(logConfigFile, 'r')))
    logger = logging.getLogger('error')
    return logger