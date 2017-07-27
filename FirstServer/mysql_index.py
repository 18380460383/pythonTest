# Bootstrap 测试
from django.shortcuts import render
from FirstServer.models import userinfo
from FirstServer import Constant,mysqlconfig

def test(request):
    return render(request,"index.html")