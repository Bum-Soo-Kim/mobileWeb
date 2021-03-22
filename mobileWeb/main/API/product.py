# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import ProductInfo
import json, requests

def renderList(request):
    return render(request,'product_list.html')

def renderDetail(request):
    return render(request,'product_detail.html')

def getList(request):
    result = {'code':'','msg':'','data':[]}

    try:
        productlist = ProductInfo.objects.all()


        
    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))