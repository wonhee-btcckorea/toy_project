# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20180622_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
