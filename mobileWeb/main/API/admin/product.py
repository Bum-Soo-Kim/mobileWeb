# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import ProductInfo
import json

def renderPage(request):
    return render(request, 'shoeproadmin/forms-validation.html')

def getList(request):
    result = {'code':'','msg':'','data':[]}

    try:
        product = ProductInfo.objects.all()
        
        for col in product:
            tmp = {'id':col.id,'name':col.name, 'price' : col.price, 'main_image' : col.main_image, 'productImage' : col.product_image}
            result['data'].append(tmp)

        result['code'] = 1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

def insertData(request):
    result = {'code':'','msg':''}

    try:
        req = request.POST

        name = req.get('name')
        price = req.get('price')
        mainUrl = req.get('main')
        subUrl = req.get('sub')

        ProductInfo.objects.create(
            name = name,
            price = price,
            main_image = mainUrl,
            product_image = subUrl,
            isSell = 'Y'
        )

        result['code'] = 1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

def deleteData(request):
    result = {'code':'','msg':''}

    try:
        idx = request.POST.get('id')
        product = ProductInfo.objects.filter(id = idx)
        product.isSell = 'N'
        product.save()

        result['code']=1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

def editData(request):
    result = {'code':'','msg':''}

    try:
        req = request.POST
        product = ProductInfo.objects


    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

    