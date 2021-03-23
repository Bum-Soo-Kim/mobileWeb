# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from main.models import ProductInfo
import json, requests

def renderPage(request):
    return render(request,'cleaninfo.html')