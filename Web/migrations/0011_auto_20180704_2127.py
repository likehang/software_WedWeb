# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-04 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0010_company_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Web.status'),
        ),
    ]
