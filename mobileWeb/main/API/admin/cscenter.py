# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from main.models import CouponList, UserCoupon, UserInfo, DB
import json

def getList(request):
    result = {'code':'','msg':''}
    db = DB().GetDB()

    try:
        cursor = db.cursor()

    finally : 
        db.close()


    return HttpResponse(json.dumps(result))