# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-31 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='status',
            field=models.CharField(choices=[('5', '结算中'), ('99', '已完成'), ('11', '退款中'), ('12', '已取消'), ('3', '安排中'), ('10', '请求退款'), ('2', '商议中'), ('4', '执行中'), ('1', '已提交'), ('25', '其他')], default='1', max_length=10),
        ),
    ]
