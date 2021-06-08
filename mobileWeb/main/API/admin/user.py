# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import UserInfo, User
import json

def renderPage(request):
    return render(request, 'shoeproadmin/users.html')

def renderDetail(request):
    return render(request, 'shoeproadmin/user_detail.html')


def getList(request):
    result = {'code':1, 'data':[],'msg':''}

    try:
        userinfo = UserInfo.objects.all()

        for idx in userinfo:
            tmp = {''}
            result['data'].append(tmp)


    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def getDetail(request):
    result = {'code':'','msg':'','data':[]} 

    try:
        user_idx = request.POST.get('idx')
        

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))