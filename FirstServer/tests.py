# Bootstrap 测试
from django.shortcuts import render
from django.http import HttpResponse
import json
from FirstServer import people
from FirstServer.modle import RetrunBean, Emplyee, Python_people

# list1[0].speak()
# str_convert = list(list1)
# import json
# a = [{1:1,"a":"a"}, {2:3,"b":"b"}]
# b = json.dumps(a)
# c = json.loads(b)
# print(b)


from django.forms.models import model_to_dict
from FirstServer.ModelConver import modleconver

from django.shortcuts import render_to_response
import pymysql

# def test(request):
#     db = pymysql.connect(user='root', db='python', passwd='mn19940708', host='localhost')
#     cursor = db.cursor()
#     cursor.execute('SELECT name,id FROM python_people ORDER BY id')
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()
#     return HttpResponse(names)


from FirstServer.models import userinfo
from FirstServer.modle import TstBean

def insert(request):
    userinfo1 = userinfo(1, '测试', '123@126.com', '测试')
    userinfo1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def insertArr(request):
    for i in range(1, 50):
        userinfo1 = userinfo(i, '测试', '123@126.com', '测试'+str(i))
        userinfo1.save()
    return HttpResponse("<p>批量添加数据添加成功！</p>")


def get(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list2 = userinfo.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = userinfo.objects.filter(id=1)

    # 获取单个对象
    response3 = userinfo.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    userinfo.objects.order_by('name')[0:2]

    # 数据排序
    userinfo.objects.order_by("id")

    # 上面的方法可以连锁使用
    # userinfo.objects.filter(name="测试").order_by("id")

    lista=[]
    # 输出所有数据
    for var in list2:
        del var._state

    list3=list(list2)
    re = RetrunBean.returnBean(1025, 'successs', TstBean.tstbean(231,'测试','326@126.com','omo'))
    #print(re.convert_to_dict())
    print(list3)
    str_m = json.dumps(re, default=modleconver.convert_to_builtin_type)
    return HttpResponse(str_m)
    #return HttpResponse("<p>" + '测试' + "</p>")


def test(request):
    # return render(request, 'test.html')
    # data = {"answer": "answer"}
    list1 = []
    for i in range(1, 100):
        name = '测试'
        p = people.people(name + str(i), i, 30 + i)
        list1.append(p)

    re = RetrunBean.returnBean(1025, 'fail', list1)
    str_m = json.dumps(re, default=modleconver.convert_to_builtin_type)
    # ensure_ascii=False用于处理中文
    return HttpResponse(str_m)
    # names = Python_people.python_people.all()  # 获取我们的数据库信息到names里
    # print(names)
