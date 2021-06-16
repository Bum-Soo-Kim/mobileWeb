# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo, DB
import json, requests

def renderPage(request):
    return render(request, 'point.html')

def getPoint(request):
    result = {'code':'','msg':'','data':[]}
    db = DB().GetDB()

    try:
        cursor = db.cursor()
        uid = request.POST.get('uid')

        sql = ("SELECT SUM(point) FROM point_history WHERE user_id = {0}").format(uid)
        if cursor.execute(sql)>0:
            data = cursor.fectchall()

            for row in data:
                print(row)

            result['code'] = 1
        else:
            result['code'] = 0

    finally:
        db.close()
