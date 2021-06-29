from django.contrib import admin
from django.http import request
from django.urls import path
from details import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('remove', views.remove, name="remove"),
    path('database', views.database, name="database"),
    path('request', views.req, name="req"),
]