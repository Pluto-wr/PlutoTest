# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/3 22:08
@FileName: serializer.py
@FuncSummary: 外键字段创建模型序列化器类
@Author: wurun
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from rest_framework import serializers
from projects.serializer import ProjectModelSerializer
from .models import Interfaces


# 对外键字段进行序列化
class InterfacesModelSerializer(serializers.ModelSerializer):
    # 1、数据库模型中的外键字段，默认会生成PrimaryKeyRelateField序列化器字段
    # 序列化输出的为外键的ID值

    # 2、StringRelatedField 此字段将被序列化为关联对象字符串表达形式(即__str__方法返回值)
    # project = serializers.StringRelatedField(label='所属项目')

    # 3、SlugRelatedField 此字段将被序列化为关联对象的指定字段数据
    # project = serializers.SlugRelatedField(slug_field='tester', read_only=True)

    # 4、使用关联对象的序列化器
    project = ProjectModelSerializer(label='所属项目', read_only=True)

    class Meta:
        model = Interfaces
        fields = '__all__'
