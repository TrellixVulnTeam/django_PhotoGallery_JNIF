# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photohost', '0007_auto_20161228_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
    ]
