# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-18 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0005_auto_20180618_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='status',
            field=models.CharField(choices=[('4', '执行中'), ('25', '其他'), ('2', '商议中'), ('11', '退款中'), ('1', '已提交'), ('99', '已完成'), ('12', '已取消'), ('10', '请求退款'), ('3', '安排中'), ('5', '结算中')], default='1', max_length=10),
        ),
    ]