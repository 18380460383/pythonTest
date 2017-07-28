#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.test  #连接mydb数据库，没有则自动创建
my_set = db.user #使用test_set集合，没有则自动创建

#查询全部
for i in my_set.find():
    print(i)
#查询name=zhangsan的
for i in my_set.find({"sex":"女"}):
    print(i)
print(my_set.find_one({"name":"女"}))