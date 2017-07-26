# Bootstrap 测试
from django.shortcuts import render
from django.http import HttpResponse
from FirstServer import Constant

def test(request):
    print("-------------------------------------------------------")
    str = ''
    if request.GET:
        str = request.GET['name']
    if not str.strip():
        str = 'name is empty'
    return HttpResponse(str)
def testPost(request):
    print("-------------------------------------------------------")
    str = ''
    if request.POST:
        str = request.POST['name']
        Constant.mysql_table=str
    if not str.strip():
        str = 'name is empty'
    return HttpResponse(str)
