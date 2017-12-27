# -*- coding: UTF-8 -*- 

import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb

from django.db import connection

class cmdbDao(object):

    def getDbInstanceList(self, search_key, offset, limit):
        cursor = connection.cursor()
        if search_key == "" or search_key is None:
            sql = "select ch.id, ch.intranet_ip_addr, cdi.* from cmdb_db_instance cdi inner join cmdb_host ch on cdi.host = ch.id limit %d, %d" % (offset, limit)
        else:
            sql = "select * from cmdb_db_instance cdi inner join cmdb_host ch on cdi.host = ch.id where limit %d, %d" % (offset, limit)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
