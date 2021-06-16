# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo, DB
import json, requests

def renderPage(request):
    return render(request, 'deliveryDetail.html')

def getData(request):
    result = {'code':'','msg':'','data':[]}
    db = DB().GetDB()

    try:
        cursor = db.cursor()
        oid = request.POST.get('oid')

    finally:
        db.close()

    return HttpResponse(json.dumps(result))