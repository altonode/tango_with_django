# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-16 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
