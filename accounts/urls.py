from django.http import request
from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.loginuser, name="loginuser"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('signup', views.registeruser, name="registeruser")
]
    