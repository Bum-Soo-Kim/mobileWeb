# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

def renderPage(request):
    return render(request, 'index.html')

def getData(request):
    result = {'code':'','msg':'','data':[]}

    try : 
        1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))
