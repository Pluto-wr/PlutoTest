# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/5 16:51:
@FileName: jwt_handler.py
@FuncSummary: 重写jwt源码中的jwt_response_payload_handler方法,更改返回的内容
@Author: wurun
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""


def jwt_response_payload_handler(token, user=None, request=None):
    """"""
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
    }