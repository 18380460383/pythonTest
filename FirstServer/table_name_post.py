from django.http import HttpResponse
from FirstServer import Constant
import json

def testPost(request):
    str = ''
    par = {}
    datalist=[]
    if request.POST:
        for key in request.POST:
            par[''+key]=request.POST[''+key]
            datalist.append(par)
            Constant.mysql_table=request.POST[''+key]
        print(json.dumps(par))
        # str = ''
        # Constant.mysql_table=str
    # if not str.strip():
    #     str = 'name is empty'
    #insert into firstserver_employee (name) VALUES('测试')
    print('+++++++++++++++++++++++' + Constant.mysql_table)
    return HttpResponse(json.dumps(par))
