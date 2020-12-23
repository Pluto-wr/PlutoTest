# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/5 18:19
@FileName: serializers.py
@FuncSummary: 用户模块序列器
@Author: wurun
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings


class RegisterSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(label='确认密码',
                                             min_length=6,
                                             max_length=20,
                                             help_text='确认密码',
                                             write_only=True,
                                             error_messages={
                                                 'min_length': '只允许6~20个字符的确认密码',
                                                 'max_length': '只允许6~20个字符的确认密码',
                                             })

    token = serializers.CharField(label='生成Token',
                                  read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        # 更改User模型类中字段
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '只允许6~20个字符的用户名',
                    'max_length': '只允许6~20个字符的用户名',
                },
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '只允许6~20个字符的密码',
                    'max_length': '只允许6~20个字符的密码',
                },
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 校验邮箱是否重复
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')]
            },
        }

    def validate(self, attrs):
        """
        校验密码
        :param attrs: 反序列化后的字典
        :return: attrs
        """
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('两次密码输入不一致!')
        return attrs

    def create(self, validated_data):
        """
        重写create
        :param validated_data: 检验后的数据
        :return: 创建的用户
        """
        validated_data.pop('password_confirm')  # 删除数据库模型类中不存在的属性
        user = User.objects.create_user(**validated_data)
        # user = super(RegisterSerializer, self).create(**validated_data)
        # user.set_password(validated_data['password'])  # 加密密码
        # user.save()
        RegisterSerializer.creat_token(user)
        return user

    @staticmethod
    def creat_token(model_obj):
        """
        手动创建token
        :param model_obj: 模型类对象
        :return:
        """
        # 手动为用户生成token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(model_obj)
        token = jwt_encode_handler(payload)
        model_obj.token = token
