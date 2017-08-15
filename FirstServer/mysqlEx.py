#!/usr/bin/python
# -*- coding: UTF-8 -*-

from FirstServer import mysqlconfig,mysqlcolunm,Constant
from django.shortcuts import render
import json
# 打开数据库连接
# db = MySQLdb.connect("localhost","root","mn19940708","information_schema" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
def show(request):
        print("++++++++++++++++++++++++++++   "+ Constant.mysql_table)
        context = {}
        context['results']=[]
        myc=mysqlconfig.mysqlCon("localhost","root","mn19940708",Constant.mysql_dataBase )
        cursor=myc.openInformation()
        # SQL 查询语句
        sql = "select column_name,COLUMN_TYPE,IS_NULLABLE from information_schema.columns where table_schema='python' and table_name='"+Constant.mysql_table+"'"
        results=[]
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 获取所有记录列表
           result = cursor.fetchall()
           for row in result:
               re={}
               re['name']=row[0]
               re['type']=row[1]
               re['null_able']=row[2]
               results.append(re)
        except:
           print ("Error: unable to fecth data")
        print(results)
        # 关闭数据库连接
        myc.db.close()
        context['table_name']=Constant.mysql_table
        context['results']=results
        return render(request, 'mysqlCloun.html',context)