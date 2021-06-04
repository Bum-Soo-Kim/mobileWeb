import logging
from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
import MySQLdb
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import birthday

# Create your models here.
class TimeModel(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    upd_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        abstract = True

#유저정보 테이블
class UserInfo(TimeModel):
    JOIN_TYPE = [
        ('normal','일반'),
        ('kakao','카카오')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length= 10, verbose_name='로그인 타입')
    phone = models.CharField(max_length=20, verbose_name='핸드폰 번호', null=True)
    birthday = models.DateField(null=True)
    
    def __int__(self):
        return self.id

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = 'auth_user_info'
        verbose_name = '유저 추가정보'
        verbose_name_plural = '유저 추가정보'

#상품정보 테이블
class ProductInfo(TimeModel):
    name = models.CharField(max_length=30, verbose_name='상품 이름')
    price = models.CharField(max_length=30, verbose_name='가격')
    main_image = models.FileField(max_length=255, verbose_name='메인 이미지')
    video_url = models.CharField(max_length=255, verbose_name='영상 url')
    product_image = models.FileField(verbose_name='상품 설명', null=True)
    isSell = models.BooleanField(verbose_name='판매 여부')

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'product_info'
        verbose_name = '상품 정보'
        verbose_name_plural = '상품 정보'

# #상품 이미지 테이블
# class ProductImage(TimeModel):
#     product = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)
#     image = models.CharField(max_length=255, verbose_name='이미지 url')
#     photo = models.FileField(null=True)

#     def __int__(self):
#         return self.id

#     class Meta:
#         db_table = 'product_image'
#         verbose_name = '상품 이미지'
#         verbose_name_plural = '상품 이미지'

#세척정보
class UseInfo(TimeModel):
    name = models.CharField(max_length=30, verbose_name='세척 이름')
    main_image = models.CharField(max_length=255, verbose_name='메인 이미지')
    text = models.TextField(verbose_name='설명')
    video_url = models.CharField(max_length=255, verbose_name='영상 url')
    product = models.ManyToManyField('ProductInfo')

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'use_info'
        verbose_name = '세척 정보'
        verbose_name_plural = '세척 정보'

#세척정보 이미지
class CleanImage(TimeModel):
    clean = models.ForeignKey('UseInfo', on_delete=models.CASCADE)
    image = models.FileField(null=True, blank = True, upload_to='test/cleanimage/')

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'use_image'
        verbose_name = '세척 이미지'
        verbose_name_plural = '세척 이미지'

#신발세척신청
class CleanInfo(TimeModel):
    CLEAN_TYPE = [
        ('BASIC 코스','basic'),
        ('PREMIUM 코스','premium')
    ]

    user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='수량')
    clean_type = models.CharField(max_length=15, choices=CLEAN_TYPE)
    isVideo = models.BooleanField(verbose_name='비디오 여부',null=True)
    isAddiServ = models.BooleanField(verbose_name='살균,탈취',null=True)
    class Meta : 
        db_table = 'clean_info'
        verbose_name = '세척 신청'
        verbose_name_plural = '세척 신청'

class SocialAccount(models.Model):
    type = models.CharField(max_length=50, verbose_name='종류')
    key = models.CharField(max_length=300, verbose_name='키 값')
    secret_key = models.CharField(max_length=300, verbose_name='secret key', null=True)

    class Meta:
        db_table = 'social_account'
        verbose_name = '소셜 계정 관리'
        verbose_name_plural = '소셜 계정 관리'

class ProductReview(TimeModel):
    user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    product = models.ForeignKey('ProductInfo',on_delete=CASCADE)
    contents = models.TextField(verbose_name='리뷰내용')

    class Meta:
        db_table = 'product_review'
        verbose_name = '상품 리뷰'
        verbose_name_plural = '상품 리뷰'

class CleanReview(TimeModel):
    user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    clean = models.ForeignKey('CleanInfo',on_delete=CASCADE)
    contents = models.TextField(verbose_name='리뷰내용')

    class Meta:
        db_table = 'clean_review'
        verbose_name = '세척 리뷰'
        verbose_name_plural = '세척 리뷰'

class OrderTable(TimeModel):
    ORDER_TYPE = [
        ('nonmem','비회원'),
        ('mem','회원')
    ]

    ordernum = models.IntegerField(verbose_name= '주문번호')
