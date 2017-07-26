#Bootstrap 测试
from django.shortcuts import render
def test(request):
     return render(request, 'mapcanvas.html')