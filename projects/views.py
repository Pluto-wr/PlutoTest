from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from projects.serializer import ProjectModelSerializer, ProjectNameSerializer, InterfacesByProjectIdSerializer
from .models import Projects
from utils.pagination import PageNumberPaginationManual


# APIView GenericAPIView
# ViewSet不再支持get, post, put, delete等请求方法，而只支持action动作
# ViewSet类中未提供get_object()，get_serializer()等方法
# 所以需要继承GenericViewSet
class ProjectsViewSet(viewsets.ModelViewSet):
    """项目类视图"""
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name', 'leader']
    filterset_fields = ['name', 'leader', 'tester']

    permission_classes = [permissions.IsAuthenticated]

    # 可以使用action装饰器来声明自定义的动作，默认情况下实例方法名就是action名
    # methods指定请求方法，默认get
    # detail用于指定该动作要处理的是否为详情资源对象（url是否需要传递pk值），单条数据设置True.列表数据返回False
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = InterfacesByProjectIdSerializer(instance=queryset)
        return Response(serializer.data)
