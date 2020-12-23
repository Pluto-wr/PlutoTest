# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/5 16:11
@FileName: urls.py
@FuncSummary: 子应用user子路由模块,使用obtain_jwt_token进行登录认证,返回token
@Author: wurun
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    # 使用obtain_jwt_token认证
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),
]