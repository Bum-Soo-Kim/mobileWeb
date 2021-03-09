# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo
import json

def renderPage(request):
    return render(request, 'join.html')

def getJoin(request):
    result = {'code':'','msg':'','uid':''}

    try:
        req = request.POST
        id = req.get('id')
        pw = req.get('pw')
        name = req.get('name')
        type = req.get('type')
        if User.objects.filter(username = id).exists():
            result['code'] = 0
            result['msg'] = '이미 존재하는 아이디 입니다'
        else:
            userinfo = User.objects.create_user(
                username = id,
                password = pw,
                first_name = name
            )
            UserInfo.objects.create(
                user = userinfo,
                type = type,
            ).save()           
            result['code'] = 1
            result['msg'] ='회원가입이 완료되었습니다'
        
    except Exception as e:
        result['code'] = -1
        raise e

    return HttpResponse(json.dumps(result))