# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 08:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledaction',
            old_name='executed',
            new_name='execute',
        ),
    ]
