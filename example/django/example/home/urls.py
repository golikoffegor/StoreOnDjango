#!/usr/bin/env python3
# -*- coding: utf-8 -*
from django.urls import path

from .import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
