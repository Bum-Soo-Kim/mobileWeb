# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from main.models import CleanReview, ProductReview
import json

def getList(request):
    result = {'code':'','msg':'','clean':[],'product':[]}

    try:
        clean = CleanReview.objects.all()
        for row in clean:
            tmp = {''}
            result['clean'].append(tmp)

        product = ProductReview.objects.all()
        for row in product:
            tmp = {''}
            result['product'].append(tmp)

        result['code']=1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(json))

