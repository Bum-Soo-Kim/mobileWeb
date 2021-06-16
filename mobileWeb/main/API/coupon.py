# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import UserCoupon, DB
import json, requests

def renderPage(request):
    return render(request, 'coupon.html')

def getList(request):
    result = {'code':'','msg':'','data':[]}
    db = DB().GetDB()

    try : 
        cursor = db.cursor()
        uid = request.POST.get('uid')

        sql = ( "SELECT                                         "
                "   cl.name         AS  name,                   "
                "   cl.price        AS  price,                  "
                "   cl.expdate      AS  exp                     "
                "FROM user_coupon uc                            "
                "JOIN coupon_list cl ON uc.coupon_id = cl.id    "
                "WHERE 1=1                                      "
                "   AND uc.user_id = {0}                        "
                "   AND uc.isUse = 'Y'                          ").format(uid)

        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)

    finally:
        db.close()

    return HttpResponse(json.dumps(result))