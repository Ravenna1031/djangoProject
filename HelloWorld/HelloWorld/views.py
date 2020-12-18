# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse


def hello(request):
    # return HttpResponse("Hello world !")
    dic = {'num': None}
    if request.GET:
        a = request.GET.get('a', 0)
        b = request.GET.get('b', 0)
        if a and b:
            dic['num'] = int(a) + int(b)
            dic = json.dumps(dic)
            return HttpResponse(dic)
        else:
            return HttpResponse("错误")
    else:
        return HttpResponse("错误")