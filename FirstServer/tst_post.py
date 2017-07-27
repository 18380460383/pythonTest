# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
import json

# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        for key in request.POST:
            valuelist = request.POST.getlist(key)
        print(valuelist)
        ctx['rlt'] = request.POST['q']
    return render(request, "tst_post.html", ctx)