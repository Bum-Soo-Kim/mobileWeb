# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo, DB
import json, requests
from iamport import Iamport

def renderPage(request):
    return render(request, 'payment.html')

def getData(request):
    result = {'code':1,'msg':'','data':[]}

    try:
        pid = request.POST.get('product')
        

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def getPayment(request):
    iamport = Iamport(imp_key = '', imp_secret='')
    #json type 
    payload = {
        ''
    }

    db = DB().GetDB()
    result = {'code':'','msg':'','data':[]}

    try:
        cursor = db.cursor()
        req = request.POST

        uid = req.get('uid')
        pid = req.get('pid')

        sql = ("")


    finally:
        db.close()

    return HttpResponse(json.dumps(result))

def writeReview(request):
    result = {'code':1,'msg':''}

    try:
        req = request.POST
        user = req.get('user')
        content = req.get('content')
        product = req.get('product')

        sql = ("INSERT INTO product_review(user_id, product_id, content) VALUES (user, product, content)")

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))
