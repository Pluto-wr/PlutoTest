# Generated by Django 2.2.9 on 2020-11-28 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0004_auto_20201129_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='接口名称', max_length=200, unique=True, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试工程师', max_length=50, verbose_name='测试工程师')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.PROTECT, to='projects.Projects', verbose_name='所属项目')),
            ],
            options={
                'db_table': 'tb_interfaces',
            },
        ),
    ]
