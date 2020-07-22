# -*- coding: UTF-8 -*- 

import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb

from django.db import connection

class Dao(object):
    _CHART_DAYS = 90

    #连进指定的mysql实例里，读取所有databases并返回
    def getAlldbByCluster(self, mainHost, mainPort, mainUser, mainPassword):
        listDb = []
        conn = None
        cursor = None
        
        try:
            conn=MySQLdb.connect(host=mainHost, port=mainPort, user=mainUser, passwd=mainPassword, charset='utf8mb4')
            cursor = conn.cursor()
            sql = "show databases"
            n = cursor.execute(sql)
            listDb = [row[0] for row in cursor.fetchall() 
                         if row[0] not in ('information_schema', 'performance_schema', 'mysql', 'test')]
        except MySQLdb.Warning as w:
            print(str(w))
        except MySQLdb.Error as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.commit()
                conn.close()
        return listDb

    def getWorkChartsByMonth(self):
        cursor = connection.cursor()
        sql = "select date_format(create_time, '%%m-%%d'),count(*) from inception_sql_order where create_time>=date_add(now(),interval -%s day) group by date_format(create_time, '%%m-%%d') order by 1 asc;" % (Dao._CHART_DAYS)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def getWorkChartsByPerson(self):
        cursor = connection.cursor()
        sql = "select engineer, count(*) as cnt from inception_sql_order where create_time>=date_add(now(),interval -%s day) group by engineer order by cnt desc limit 50;" % (Dao._CHART_DAYS)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
