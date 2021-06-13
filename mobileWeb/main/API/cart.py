# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import CleanInfo, CleanBasket, ProductBasket, ProductInfo
import json, requests

def renderPage(request):
    return render(request, 'cart.html')

def addProduct(request):
    result = {'code':'','msg':''}

    try :
        req = request.POST
        type = req.get('type')
        id = req.get('id')
        user = req.get('user')

        if type == 'product':
            ProductBasket.objects.create(
                user = user,
                product = id
            )
        else:
            CleanBasket.objects.create(
                user = user,
                clean = id
            )

    except Exception as e:
        raise e 

    return HttpResponse(json.dumps(result))


def deleteProduct(request):
    result = {'code':'','msg':''}

    try:
        req = request.POST
        type = req.get('type')
        uid = req.get('user')
        bid = req.get('id')

        if type == 'clean':
            obj = CleanBasket.objects.filter(user = uid, clean = bid)
        else:
            obj = ProductBasket.objects.filter(user = uid, product = bid)

        obj.delete()
        result['code'] = 1

    except Exception as e:
        result['code'] = e
        result['msg'] = e
        raise e

    return HttpResponse(json.dumps(result))

def getBasketList(request):
    result = {'code':'','msg':'','product':[],'clean':[]}

    try:
        uid = request.POST.get('user')
        product = ProductBasket.objects.filter(user = uid)
        clean = CleanBasket.objects.filter(user = uid)

        for row in product:
            pid = row.product
            pobj = ProductInfo.objects.filter(id = pid)
            for obj in pobj:
                if obj.isSell == 'Y':
                    tmp = {'id':obj.id,'name':obj.name, 'price':obj.price,'image':obj.main_image}
                result['product'].append(tmp)

        for row in clean:
            cid = row.clean

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))