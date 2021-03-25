# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo
import json, requests

def renderPage(request):
    return render(request)

def getData(request):
    result = {'code':'','msg':'','data':[]}

    return HttpResponse(json.dumps(result))

def estimateInfo(request):
    result = {'code':'','msg':'','data':[]}
    
    try:
        req = request.POST
        cnt = req.get('cnt')
        uid = req.get('uid')
        cleantype = req.get('cleantype')
        isVideo =req.get('isVideo')
        isAddi = req.get('isAddi')

        CleanInfo.objects.create(
            user = uid,
            count = cnt,
            clean_type = cleantype,
            isVideo = isVideo,
            isAddiserv = isAddi,
        ).save()
        result['code']=1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

