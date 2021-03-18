# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import json, requests

def renderPage(request):
    return render(request)

def getData(request):
    result = {'code':'','msg':'','data':[]}

    return HttpResponse(json.dumps(result))

def estimateInfo(request):
    result = {'code':'','msg':'','data':[]}

    return HttpResponse(json.dumps(result))