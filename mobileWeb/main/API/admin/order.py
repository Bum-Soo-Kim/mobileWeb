# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import OrderTable
import json

def getList(request):
    result = {'code':'','msg':'','data':[]}

    try:
        object = []

        for row in object:
            tmp = {}
            result['data'].append(tmp)
        result['code']=1
    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def getDetail(request):
    result = {'code':'','msg':'','data':[]}

    try:
        idx = request.POST.get('id')

        info = OrderTable.objects.filter(id = idx)
        for row in info:
            tmp = {'id':row.id, 'orderid':row.orderId, 'address':row.address, 'subaddr':row.subaddr, 
                    'company':row.company, 'invoice':row.invoice, 'payment':row.payment}
            result['data'].append(tmp)

        result['code']=1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))
