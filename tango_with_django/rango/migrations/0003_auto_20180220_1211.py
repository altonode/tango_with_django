# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180216_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc)),
        ),
    ]
