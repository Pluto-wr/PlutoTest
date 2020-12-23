from django.db import models


# Create your models here.
# 一个项目中有多个接口，那么需要在”多“的一创建外键，项目表为父表("一")。接口表为子表("多")
class Interfaces(models.Model):

    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    tester = models.CharField(verbose_name='测试工程师', max_length=50, help_text='测试工程师')
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    # ForeignKey第一个参数为关联的模型路径或者模型类，也可以导入模型类直接使用
    # on_delete设置当父表删除之后该字段的处理方式 必传。CASCADE --> 子表也会被删除。
    # SET_NULL --> 当前外键值会被置为None
    # PROJECT --> 会报错
    # SET_DEFAULT --> 设置默认值， 同时需要指定默认值，null=True
    project = models.ForeignKey('projects.Projects', on_delete=models.PROTECT, verbose_name='所属项目', help_text='所属项目')

    class Meta:
        db_table = 'tb_interfaces'

    def __str__(self):
        return self.name
