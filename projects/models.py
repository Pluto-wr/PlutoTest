from django.db import models


# Create your models here.
# 1、每一个应用下的数据库模型类，models.py定义， 数据库模型类必须继承models.Model
# 2、一个数据库模型相当与一个数据表
# 3、定义的类属性就相当于数据库表中的字段
# 4、默认会创建一个默认递增的id主键
# 5、默认创建的数据库名为 应用名小写_数据库模型类小写
class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # objects = models.Manager()  # 加上这句才能应用objects

    # class Meta:
    #     verbose_name = '人类'
    #     verbose_name_plural = '人类'


class Projects(models.Model):

    # max_length为字段最大长度， unique用与设置当前字段是否唯一，默认为False
    # verbose_name用于设置更人性化的字段名，相当于别名
    # help_text用于api文档中的一个中文名称
    name = models.CharField(verbose_name='项目名称', max_length=200, unique=True, help_text='项目名称')
    leader = models.CharField(verbose_name='负责人', max_length=50, help_text='负责人')
    tester = models.CharField(verbose_name='测试工程师', max_length=50, help_text='测试工程师')
    programer = models.CharField(verbose_name='开发工程师', max_length=50, help_text='开发工程师')
    publish_app = models.CharField(verbose_name='发布应用', max_length=100, help_text='发布应用')
    # TextField 文本字段
    # null设置数据库中此字段允许为空 blank用于设置前端可以不传递 default设置默认值
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    # 元类Meta,用于设置当前数据模型的元数据信息
    class Meta:
        # 设置表名
        db_table = 'tb_projects'
        # 会在admin站点中，显示一个更人性化的表名
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
