# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 11:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AudioUpload',
            new_name='AudioFile',
        ),
    ]