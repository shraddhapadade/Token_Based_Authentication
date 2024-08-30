from .views import *
from django.contrib import admin
from django.urls import path, include
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView


urlpatterns=[
    path("login/", UserLoginAPIView.as_view(), name="home_login"),
    path("register/", UserRegisterAPIView.as_view(), name="home_register"),
    path("logout/", UserLogoutAPIView.as_view(), name="home_logout")
]
