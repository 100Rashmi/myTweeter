# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20171105_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_id',
            field=models.CharField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
