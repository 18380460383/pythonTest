# Bootstrap 测试
from django.shortcuts import render
from FirstServer.models import userinfo
from FirstServer import Constant,mysqlconfig

def test(request):
    clomunList=getColumn()

    context = {}
    context['results'] = []
    myc = mysqlconfig.mysqlCon("localhost", "root", "mn19940708",'python')
    cursor = myc.openInformation()
    # SQL 查询语句
    sql = "select * from " + Constant.mysql_table + ""
    results = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        # for row in result:
        #     re = {}
        #     re['name'] = row[0]
        #     re['type'] = row[1]
        #     re['null_able'] = row[2]
        #     results.append(re)
    except:
        print("Error: unable to fecth data")
    print(result)
    # 关闭数据库连接
    myc.db.close()
    context['cloum'] = clomunList
    context['results'] = result
    #return render(request, 'table_show.html',context)
    return render(request, 'table_data_tables.html',context)

def getColumn():
    context = {}
    context['results'] = []
    myc = mysqlconfig.mysqlCon("localhost", "root", "mn19940708",'information_schema')
    cursor = myc.openInformation()
    # SQL 查询语句
    sql = "select column_name from information_schema.columns where table_schema='python' and table_name='" + Constant.mysql_table + "'"
    results = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        for item in result:
            results.append(item[0])
        print(results)
    except:
        print("Error: unable to fecth data")
    print(results)
    # 关闭数据库连接
    myc.db.close()
    return results
