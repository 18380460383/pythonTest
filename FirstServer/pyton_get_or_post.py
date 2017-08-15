# Bootstrap 测试
from django.shortcuts import render
from django.http import HttpResponse
from FirstServer import Constant,mysqlconfig
import json
from FirstServer.dss.Serializer import Serializer

def test(request):
    str = ''
    if request.GET:
        str = request.GET['name']
    if not str.strip():
        str = 'name is empty'
    return HttpResponse(str)
def testP(request):
    str = ''
    if request.POST:
        str = request.POST['name']
    if not str.strip():
        str = 'name is empty'
    return HttpResponse(str)
def testPost(request):
    str = ''
    par = {}
    datalist=[]
    sql='insert into '+Constant.mysql_table
    sqlCloum='('
    sqlValue='VALUES('
    if request.POST:
        lengt=len(request.POST)-1
        for i,key in enumerate(request.POST):
            sqlCloum=sqlCloum+ key
            par[''+key]=request.POST[''+key]
            sqlValue=sqlValue+"'"+request.POST[''+key]+"'"
            datalist.append(par)
            if i<lengt:
                sqlCloum=sqlCloum+' , '
                sqlValue=sqlValue+' , '
            else:
                sqlCloum=sqlCloum+')'
                sqlValue=sqlValue+')'
        sql=sql+sqlCloum+sqlValue
        print(json.dumps(par))
        print(sql)
        myc = mysqlconfig.mysqlCon("localhost", "root", "mn19940708", "python")
        cursor = myc.openInformation()
        # SQL 查询语句
        #sql = "select table_name from information_schema.tables where table_schema='python' and table_type='base table'"
        results = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            myc.db.commit()
            par['code']='10000'
            par['msg']='插入成功'
        except:
            par['code'] = '10002'
            par['msg'] = '插入失败'
            print("Error: unable to fecth data")
            myc.db.rollback()
        #print(results)
        # 关闭数据库连接
        myc.db.close()
        # str = ''
        # Constant.mysql_table=str
    # if not str.strip():
    #     str = 'name is empty'
    #insert into firstserver_employee (name) VALUES('测试')
    return HttpResponse(json.dumps(par))
