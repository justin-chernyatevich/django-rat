# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 13, 24, 32, 443577), verbose_name='Дата добавления'),
            preserve_default=False,
        ),
    ]