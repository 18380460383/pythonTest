# Bootstrap 测试
from django.shortcuts import render,HttpResponse
from FirstServer import Constant, mysqlconfig
from FirstServer.modle import RetrunBean
import json
from FirstServer.ModelConver import modleconver
def test(request):
    return render(request,"login.html")
def loginJ(request):
    if request.POST:

        myc = mysqlconfig.mysqlCon(Constant.mysql_add, Constant.mysql_user, Constant.mysql_pass, 'python')
        cursor = myc.openInformation()
        # SQL 查询语句
        sql = "select * from " + "firstserver_user where "
        lengt = len(request.POST) - 1
        whereV=''
        for i, key in enumerate(request.POST):
            if i < lengt:
                whereV=whereV+' '+key+" = '"+request.POST[''+key]+" ' and"
            else:
                whereV = whereV + ' ' + key + " = '" + request.POST['' + key] + " ' "
        sql=sql+whereV
        print(sql)
        re=None
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            if len(result)>0:
             re = RetrunBean.returnBean(10000, 'successs',None)
            else:
             re = RetrunBean.returnBean(10001, 'faile', None)
        except:
            print("Error: unable to fecth data")
        print(re)
        # 关闭数据库连接
        myc.db.close()

    return HttpResponse(json.dumps(re, default=modleconver.convert_to_builtin_type))
