# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_observedcharacteristic_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observedcharacteristic',
            name='item',
        ),
    ]
