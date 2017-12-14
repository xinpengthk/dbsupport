import logging
import logging.config
from os.path import os

from django.test import TestCase
import yaml


# Create your tests here.
if __name__ == '__main__':
    logConfigFile = r"../dbsupport/logConfig.yaml"
    print(logConfigFile)
    print(os.path.abspath(logConfigFile))
    logging.config.dictConfig(yaml.load(open(logConfigFile, 'r')))
    #logging.config.fileConfig('logger.conf')
    # create logger
    logger = logging.getLogger('error')
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')  