# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('last_seen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastseen',
            name='module',
            field=models.CharField(default='default', max_length=20),
        ),
    ]
