#!/usr/bin/python
# -*- coding: UTF-8 -*-

from FirstServer import mysqlconfig,mysqlcolunm
from django.shortcuts import render

def show(request):
        context = {}
        context['results']=[]
        myc=mysqlconfig.mysqlCon("localhost","root","mn19940708","information_schema" )
        cursor=myc.openInformation()
        # SQL 查询语句
        sql = "select table_name from information_schema.tables where table_schema='python' and table_type='base table'"
        results=[]
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 获取所有记录列表
           result = cursor.fetchall()
           for row in result:
               re={}
               re['name']=row[0]
               results.append(re)
        except:
           print ("Error: unable to fecth data")
        print(results)
        # 关闭数据库连接
        myc.db.close()
        context['results']=results
        return render(request, 'tableShow.html',context)