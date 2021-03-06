# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-18 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0006_auto_20180618_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_ident',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order_list',
            name='status',
            field=models.CharField(choices=[('1', '已提交'), ('3', '安排中'), ('12', '已取消'), ('2', '商议中'), ('4', '执行中'), ('25', '其他'), ('10', '请求退款'), ('99', '已完成'), ('11', '退款中'), ('5', '结算中')], default='1', max_length=10),
        ),
    ]
