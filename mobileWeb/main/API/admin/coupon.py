# -*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from main.models import CouponList, UserCoupon, UserInfo
import json

def couponList(request):
    result = {'code':'','msg':'','data':[]}

    try:
        coupon = CouponList.objects.all()

        for row in coupon:
            tmp = {'name':row.name, 'price':row.price}
            result['data'].append(tmp)

        result['code']=1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def newCoupon(request):
    result = {'code':'','msg':''}

    try:
        req = request.POST
        name = req.get('name')
        price = req.get('name')
        expdate = req.get('expdate')
        CouponList.objects.create(
            name = name,
            price = price,
            expdate = expdate,
            isUse = 'Y'
        )

        result['code']=1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

def deleteCoupon(request):
    result = {'code':'','msg':''}

    try:
        idx = request.POST.get('idx')
        coupon = CouponList.objects.filter(id = idx)
        coupon.isUse='N'
        coupon.save()

        result['code']=1

    except Exception as e:
        raise e
    return HttpResponse(json.dumps(result))

def addToUser(request):
    result = {'code':'','msg':''}

    try:
        req = request.POST
        userid = req.get('user')
        cid = req.get('coupon')
        UserCoupon.objects.create(
            user = userid,
            coupon = cid,
            isUse = 'Y'
        )
        result['code']=1

    except Exception as e:
        raise e

    return HttpResponse(json.dumps(result))

