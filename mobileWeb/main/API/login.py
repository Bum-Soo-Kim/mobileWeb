# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import json

def renderPage(request):
    return render(request, 'login.html')

def getLogin(request):
    result = {'code':'','msg':''}

    try:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        user = authenticate(username = id, password = pw)
        if user is None:
            result['code'] = 0
            result['msg'] = '아이디 또는 비밀번호를 확인해주세요'
        else:
            print(login(request, user))
            result['code'] = 1

    except Exception as e:
        result['code'] = e
        result['msg'] = e

    return HttpResponse(json.dumps(result))
