# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/4 00:32
@FileName: urls.py
@FuncSummary: projects应用子路由
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from projects import views

# 1、创建SimpleRouter路由对象
# router = routers.SimpleRouter()
router = routers.DefaultRouter()
# 2、注册路由
# 第一个参数prefix为路由前缀。一般添加应用名称
# 第二个参数viewset为视图集。不用添加as_view
router.register(r'projects', views.ProjectsViewSet)


urlpatterns = [
    # 将自动生成的路由添加urlpatterns中
    path('', include(router.urls)),


]

# 方式2
# urlpatterns += router.urls
