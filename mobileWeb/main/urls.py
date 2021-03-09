from django.urls import path

from .API import main, login, join

urlpatterns = [
    #메인페이지
    path('main/',main.renderPage),

    #로그인 페이지
    path('login/',login.renderPage),

    #회원가입 페이지
    path('join/',join.renderPage),
    path('join/getJoin',join.getJoin),
]