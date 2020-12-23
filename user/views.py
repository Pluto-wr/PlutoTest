from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from . import serializers


# Create your views here.
class RegisterView(CreateAPIView):
    """注册视图类, 可以不指定queryset(获取详情时需要指定)"""

    serializer_class = serializers.RegisterSerializer
