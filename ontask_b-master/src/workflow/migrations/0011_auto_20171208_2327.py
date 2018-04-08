# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_auto_20171208_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='valid_from',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Column valid from', null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='valid_to',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Column valid until', null=True),
        ),
    ]
