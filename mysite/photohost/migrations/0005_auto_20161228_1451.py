# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photohost', '0004_photo_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(default='DEFAULT VALUE', on_delete=django.db.models.deletion.CASCADE, to='photohost.Album'),
        ),
    ]
