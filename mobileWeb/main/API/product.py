# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import ProductInfo, DB
import json
import requests


def renderList(request):
    return render(request, 'product_list.html')


def renderDetail(request):
    return render(request, 'product_detail.html')


def getList(request):
    result = {'code': '', 'msg': '', 'data': []}

    try:
        productlist = ProductInfo.objects.filter(isSell = 'Y')
        for row in productlist:
            jsondata = {'pid': row.pid, 'name': row.name, 'price': row.price, 'mainImage' : row.main_image}
            result['data'].append(jsondata)

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))


def getDetail(request):
    result = {'code': '', 'msg': '', 'data': []}

    try:
        pid = request.POST.get('pid')
        product = ProductInfo.objects.filter(id=pid)
        for row in product:
            jsondata = {'pid': row.pid, 'name': row.name, 'price': row.price, 'mainImage' : row.main_image, 'productImage':row.product_image}
            result['data'].append(jsondata)

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def newProduct(request):
    result = {'code' : 1, 'msg':''}

    try:
        req = request.POST

        name = req.get('name')
        main = req.get('mainImage')
        price = req.get('price')
        text = req.get('text')

        insert = ProductInfo.objects.create(
            name = name,
            main_image = main,
            price = price,
            text = text
        )

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def editProduct(request):
    result = {'code':1, 'msg':''}

    try:
        req = request.POST
        
        name = req.get('name')
        main = req.get('mainImage')
        price = req.get('price')
        text = req.get('text')

        
        

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))


def writeReview(request):
    result = {'code':'','msg':''}
    db = DB().GetDB()

    try:
        cursor = db.cursor()
        req = request.POST

        uid = req.get('uid')
        text = req.get('text')
        pid = req.get('pid')

        sql = ( "INSERT INTO product_review (user_id, product, contents)"
                "VALUES ({0}, {1}, {2})                 ").format(uid,text,pid)
        
        if cursor.execute(sql)>0:
            result['code'] = 1
            result['msg'] = '리뷰가 작성됫다네'
        else:
            result['code'] = 0
    finally:
        db.close()

    return HttpResponse(json.dumps(result))
