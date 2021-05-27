# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import ProductInfo
import json
import requests


def renderList(request):
    return render(request, 'product_list.html')


def renderDetail(request):
    return render(request, 'product_detail.html')


def getList(request):
    result = {'code': '', 'msg': '', 'data': []}

    try:
        productlist = ProductInfo.objects.all()
        for row in productlist:
            jsondata = {'pid': row.pid, 'name': row.name, 'price': row.price}
            result['data'].append(jsondata)

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))


def getDetail(request):
    result = {'code': '', 'msg': '', 'data': []}

    try:
        pid = request.POST.get('pid')
        product = ProductInfo.objects.filter(id=pid)
        tmp = []
        for row in product:
            tmp.append(row)

        print(tmp)

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

    