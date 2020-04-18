#!/usr/bin/env python3
# -*- coding: utf-8 -*
from django.urls import path

from . import views

app_name = 'tovar'
urlpatterns = [
 path('', views.index, name='index'),
 path('<int:id_tovar>/', views.show, name='show'),
 path('<int:id_tovar>/edit/', views.edit, name='edit'),
 path('<int:id_tovar>/delete/', views.delete, name='delete'),
 path('<int:id_tovar>/tags/', views.tags, name='tags'),
 path('<int:id_tovar>/<str:pk_tag>/drop/', views.drop_tag, name='drop_tag'),
 path('<int:id_tovar>/add_picture/', views.add_picture, name='add_picture'),
 path('<int:id_tovar>/picture/', views.picture, name='picture'),
 path('create/', views.create, name='create'),
 path('groups/', views.group_index, name='allgroups'),
 path('graph/', views.graph, name='graph'),
]
