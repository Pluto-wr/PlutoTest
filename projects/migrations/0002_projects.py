# Generated by Django 2.2.9 on 2020-11-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试工程师', max_length=50, verbose_name='测试工程师')),
                ('programer', models.CharField(help_text='开发工程师', max_length=50, verbose_name='开发工程师')),
                ('publish_app', models.CharField(help_text='发布应用', max_length=100, verbose_name='发布应用')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
            ],
        ),
    ]
