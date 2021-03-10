# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, requests

class KAKAO:
    def getUri(key):
        login_uri = 'https://kauth.kakao.com/oauth/authorize?'
        redirect_uri = 'http://127.0.0.1:8000/join/redirect'
        login_uri += 'client_id='+key+'&redirect_uri='+redirect_uri+'&response_type=code'

        return login_uri

    def getToken(key,code):
        redirect_uri = 'http://127.0.0.1:8000/join/redirect'
        access_uri = 'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id='+key+'&redirect_uri='+redirect_uri+'&code='+code
        token_data = requests.get(access_uri).json()

        return token_data
    
    def getProfile(access_token):
        token = str(access_token)
        profile_uri = 'https://kapi.kakao.com/v2/user/me?access_token='+token
        profile_data = requests.get(profile_uri).json()

        return profile_data