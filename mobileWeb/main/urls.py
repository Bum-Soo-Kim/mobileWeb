from django.urls import path

from .API import main, login, join, howto,clean, wrap, payment, about,cart, shoplist, shopinfo, coupon, point, cscenter, delivery_detail, rtf_detail, mydelivery, myinfo,\
    myitemdelivery, mypage, myreview
from .API.admin import main as admin_main, user, product

urlpatterns = [
    #메인페이지
    path('main/',main.renderPage),

    #로그인 페이지
    path('login/',login.renderPage),
    path('login/getLogin',login.getLogin),

    #회원가입 페이지
    path('join/',join.renderPage, name = 'join'),
    path('join/redirect',join.redirectPage,name='redirect'),
    path('join/getJoin',join.getJoin),
    path('join/kakaoJoin',join.kakaoLogin),
    path('join/getCertificate',join.getCertificate),
    path('join/checkID',join.checkID),

    #howto
    path('howto/',howto.renderPage),

    #clean
    path('cleanservice/',clean.renderPage),

    #wrap
    path('wrapservice/',wrap.renderPage),

    #payment
    path('payment/',payment.renderPage),

    #about
    path('about/',about.renderPage),

    #cart
    path('cart/',cart.renderPage),

    #shotlist
    path('shoplist/',shoplist.renderPage),

    #shopinfo
    path('shopinfo/',shopinfo.renderPage),

    #coupon
    path('coupon/',coupon.renderPage),

    #point
    path('point/',point.renderPage),

    #cscenter
    path('cscenter/',cscenter.renderPage),

    #delivery Detail
    path('deliveryDetail/',delivery_detail.renderPage),

    #rtf Detail
    path('rtfDetail/', rtf_detail.renderPage),
    
    #mydelivery
    path('mydelivery/',mydelivery.renderPage),

    #myinfo
    path('myinfo/',myinfo.renderPage),

    #myitemdelivery
    path('myitemdelivery/',myitemdelivery.renderPage),

    #mypage
    path('mypage/',mypage.renderPage),

    #myreview
    path('myreview/',myreview.renderPage),
]

adminurlpath =[
    path('',admin_main.renderPage),
    path('user/',user.renderPage),
    path('product/',product.renderPage)
]