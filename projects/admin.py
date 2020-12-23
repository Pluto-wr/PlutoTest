from django.contrib import admin
from .models import Projects, Person
# Register your models here.


# 注册到admin站点
# 指定站点需要显示的字段
@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    # 指定在修改（新增）中需要显示的字段
    fields = ['name', 'leader', 'tester', 'programer', 'publish_app']

    # 指定要在admin站点显示的字段
    list_display = ('id', 'name', 'leader', 'tester')
