# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photohost', '0008_remove_photo_album'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-timestamp']},
        ),
    ]
