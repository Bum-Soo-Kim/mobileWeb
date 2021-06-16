# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo, DB
import json
import requests


def renderPage(request):
    return render(request, 'clean.html')


def getData(request):
    result = {'code': '', 'msg': '', 'data': []}

    return HttpResponse(json.dumps(result))


def estimateInfo(request):
    result = {'code': '', 'msg': '', 'data': []}

    try:
        req = request.POST
        cnt = req.get('cnt')
        uid = req.get('uid')
        cleantype = req.get('cleantype')
        isVideo = req.get('isVideo')
        isAddi = req.get('isAddi')

        CleanInfo.objects.create(
            user=uid,
            count=cnt,
            clean_type=cleantype,
            isVideo=isVideo,
            isAddiserv=isAddi,
        ).save()
        result['code'] = 1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))


def askQuestion(request):
    result = {'code': '', 'msg': '', 'data': []}
    db = DB().GetDB()

    try:
        cursor = db.cursor()
        uid = request.POST.get('uid')
        cid = request.POST.get('cid')

        sql = ( "INSERT INTO clean_ask ()    "
                "VALUES ()")

        if cursor.execute(sql)>0:
            result['code'] = 1
            result['msg'] = '문의 완료'
        else:
            result['code'] = 0
            result['msg'] = 'fail'

    finally:
        db.close()

    return HttpResponse(json.dumps(result))