# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-18 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busticketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Band',
            new_name='Busticketing_band',
        ),
    ]