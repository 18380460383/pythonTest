import hashlib
from django.http import HttpResponse
def md5(str1):
    import hashlib
    import types
    if isinstance(str1,str):
        m = hashlib.md5(str1.encode('gb2312'))
        #m = hashlib.md5()
        #m.update(str1)
        return m.hexdigest()
    else:
        return ''
def test(request):
    return HttpResponse(md5('测试'))