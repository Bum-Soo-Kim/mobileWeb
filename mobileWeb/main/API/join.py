# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from main.models import UserInfo, SocialAccount
from .common.kakao import KAKAO
import json, requests

def renderPage(request):
    return render(request, 'join.html')

def redirectPage(request):
    result={'code':'','msg':''}

    try : 
        code = request.GET['code']
        key = SocialAccount.objects.filter(type = 'kakao_rest_api').get().key
        token = KAKAO.getToken(key,code)
        access_token = token['access_token']

        profile_data = KAKAO.getProfile(access_token)
        id = profile_data['id']
        kid = 'kakao_'+str(id)
        name = profile_data['properties']['nickname']

        if User.objects.filter(username = kid).exists():
            user = authenticate(username = kid, password = id)
            if user is None:
                result['code'] = 0
                result['msg'] = '이미 가입한 아이디 입니다.'
            else:
                result['code'] = 1
                login(request, user)
        else:
            kuser = User.objects.create_user(
                username = kid,
                password = id,
                first_name = name
            )
            UserInfo.objects.create(
                user = kuser,
                type = 'kakao'
            ).save()
            result['code'] = 1
            result['msg'] = '회원가입이 완료되었습니다.'

    except Exception as e:
        result['code'] = e
        result['msg'] = e

    return redirect('join')

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

def kakaoLogin(request):
    result = {'code':'','msg':''}

    try:
        key = SocialAccount.objects.filter(type = 'kakao_rest_api').get().key
        login_uri = KAKAO.getUri(key)

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise(e)

    return redirect(login_uri)

def getCertificate(request):
    result = {'code':'','msg':'','key':''}

    try:
        key = SocialAccount.objects.filter(type = 'iamport_test').get().key
        result['key'] = key

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))