# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.db.models.expressions import F
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import DB
import json, requests

def renderPage(request):
    return render(request, 'mydelivery.html')

def getData(request):
    result = {'code':'','msg':'','data':[]}
    db = DB().GetDB()

    try:
        req = request.POST
        uid = req.get('uid')
        cursor = db.cursor()

        productsql = (  "SELECT  "
                        "   po.order_id     AS  orderid,    "
                        "   po.address      AS  address,    "
                        "   po.subaddr      AS  subaddr,    "
                        "   po.company      AS  company,    "
                        "   po.invoice      AS  invoice,    "
                        "   po.paymnet      AS  payment,    "
                        "   po.price        AS  price       "
                        "FROM product_order po              "
                        "JOIN "
                        "WHERE po.user_id = {0}             ").format(uid)

        cleansql = ("SELECT     "
                    "   co.order_id     AS  orderid,    "
                    "   co.address      AS  address,    "
                    "   co.subaddr      AS  subaddr,    "
                    "   co.company      AS  company,    "
                    "   co.invoice      AS  invoice,    "
                    "   co.payment      AS  payment,    "
                    "   co.price        AS  price       "
                    "FROM clean_order co                "
                    "JOIN"
                    "WHERE co.user_id = {0}             ").format(uid)
        
        sql = productsql + 'UNION\n' + cleansql
        cursor.execute(sql)
        tmp = DB().convertFetch2Json(cursor,False)
        
        for row in tmp:
            print(row)
        
    finally:
        db.close()

    return HttpResponse(json.dumps(result))

def getDetail(request):
    result = {'code':'','msg':'','data':[]}
    db = DB().GetDB()

    try:
        cursor = db.cursor()
        req = request.POST
        uid = req.get('uid')
        pid = req.get('pid')
        type = req.get('type')

        if type == 'product':
            sql = ( "SELECT  * "
                    "FROM product_order po  "
                    "JOIN product_info pi ON po.product_id = pi.id  "
                    "WHERE po.id = {0}  ").format(pid)
        elif type == 'clean':
            sql = ( "SELECT *    "
                    "FROM clean_order co    "
                    "JOIN clean_info ci ON co.clean_id = ci.id  "
                    "WHERE ci.id = {0}  ").format(pid)

        cursor.execute(sql)
        data = db.convertFetch2Json(cursor,False)

        for row in data:
            print(row)

    finally:
        db.close()

    return HttpResponse(json.dumps(result))
