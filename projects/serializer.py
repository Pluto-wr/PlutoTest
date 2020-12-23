# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/30 21:52
@FileName: serializer.py
@FuncSummary: rest framework 序列化器
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Projects
from interfaces.models import Interfaces


# 创建自定义校验器，第一个参数为字段的值
def is_unique_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError('项目名中必须包含“项目”')


# 1、继承Serializer类或子类
class ProjectSerializer(serializers.Serializer):
    """创建项目序列化器类"""
    # label变量相当于verbose_name,help_text， 设置别名
    # 字段需与Model类中一一对应
    # ！！！ 需要输出那些字段，在序列化器类中就定义那些字段，没定义的字段不会序列化输出！！！
    # 定义的序列化器字段，默认既可以序列化输出，也可以反序列化输入
    # read_only=True 指定该字段只能进行序列化输出，不能反序列化输入
    id = serializers.IntegerField(label='ID', read_only=True)
    # write_only=True 指定该字段只能进行反序列化输入，不能序列化输出
    # error_messages自定义校验错误提示
    name = serializers.CharField(label='项目名称', max_length=200,
                                 help_text='项目名称', write_only=True,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'),
                                             is_unique_project_name],
                                 error_messages={"max_length": '长度不能超过200个字节'})
    leader = serializers.CharField(label='负责人', max_length=50, min_length=6, help_text='负责人',
                                   error_messages={"min_length": '长度不能少于6个字节', "max_length": '长度不能超过50个字节'},)
    tester = serializers.CharField(label='测试工程师', max_length=50, help_text='测试工程师')
    programer = serializers.CharField(label='开发工程师', max_length=50, help_text='开发工程师')
    publish_app = serializers.CharField(label='发布应用', max_length=100, help_text='发布应用')
    # allow_null相当于模型类中的null参数, allow_blank相当于模型类中的blank
    desc = serializers.CharField(label='简要描述', allow_null=True, help_text='简要描述', allow_blank=True, default='')

    # 序列化器内部单字段的校验器, 必须以validate_开头， value为前端传入的值
    # 字段校验器的顺序
    # 字段定义时的限制（包含validators列表条目从左到右校验） -> 单字段的校验（validate_字段名）-> 多字段联合校验，validate
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        # 单字段的校验器检验成功后， 一定要返回value
        return value

    def validate(self, attrs):
        """多字段联合校验"""
        if 'Pluto' not in attrs['tester'] and 'Pluto' not in attrs['leader']:
            raise serializers.ValidationError('pluto必须在tester或leader中')
        return attrs

    # 创建项目
    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    # 4、更新项目,左侧数据库，右侧前端输入数据
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    """1、模型序列化器类, 继承ModelSerializer，自动生成Model类对应字段
        2、会自动创建create与update"""

    # 如果在模型序列化器类中定义一个类属性与Model类字段相同，
    # 则定义的类属性会覆盖掉模型序列化器类自动生成的模型类的字段。
    # 会覆盖掉Model中的name字段
    name = serializers.CharField(label='项目名称', max_length=200,
                                 help_text='项目名称',
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'),
                                             is_unique_project_name])

    # Meta子类，属性名都是固定
    class Meta:
        # 1、指定哪一个模型类来创建model
        model = Projects
        # 2、指定为模型类的那些字段，来生成序列化器
        fields = "__all__"  # 返回所有字段
        # 正向指定需要序列化输出的字段
        # fields = ('id', 'name', 'leader', 'tester', 'programer')
        # 反向指定不需要序列化输出的字段
        # exclude = ('publish_app', 'desc')

        # read_only_fields手动指定只读字段, 只能序列化输出， 且会自动加上read_only=True
        # read_only_fields = ('leader', 'tester')

        # extra_kwargs只能是嵌套字典字典的类型，自定义需要更改的字段内容，把需要更改的字段名当成key，更改的内容指定为value
        extra_kwargs = {
            'leader': {
                # 'write_only': True,
                'error_messages': {'max_length': '最大长度不超过50个字节'},
            }
        }

    # 序列化器内部单字段的校验器, 必须以validate_开头， value为前端传入的值
    # 字段校验器的顺序
    # 字段定义时的限制（包含validators列表条目从左到右校验） -> 单字段的校验（validate_字段名）-> 多字段联合校验，validate
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        # 单字段的校验器检验成功后， 一定要返回value
        return value

    def validate(self, attrs):
        """多字段联合校验"""
        if 'Pluto' not in attrs['tester'] and 'Pluto' not in attrs['leader']:
            raise serializers.ValidationError('pluto必须在tester或leader中')
        return attrs


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester')


class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
    # 指定子表序列化器，反向查询主表
    interfaces_set = InterfacesNamesSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces_set')


