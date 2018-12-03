#£¡/usr/bin/env python
#-*- coding:utf-8 -*-
# author: qiuxiang
# datetime: 2018/10/31 20:23
# software: PyCharm
# project: adminset
from django.urls import path
from navi import views


urlpatterns = [
    path('', views.index, name='navi'),
    path('add/', views.add, name='add'),
    path('manage/', views.manage, name='manage'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
]