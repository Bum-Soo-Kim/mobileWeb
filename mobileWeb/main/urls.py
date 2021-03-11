from django.urls import path

from .API import main, login, join

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
    path('join/getCertificate',join.getCertificate)
]