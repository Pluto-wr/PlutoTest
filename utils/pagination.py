# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/12/3 00:25
@FileName: pagination.py
@FuncSummary: 定制分页类
@Author: wuurn
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    # 更改源码page为p
    page_query_param = 'p'
    # 默认情况下显示的条数为2
    # 指定page_size类属性后，前端就能自定义分类条数
    page_size = 2
    page_size_query_param = 's'
    max_page_size = 50  # 指定前端能分页的最大pagesize
