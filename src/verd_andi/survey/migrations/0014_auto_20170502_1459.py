# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20170502_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcommentary',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='itemcommentary',
            name='vat',
            field=models.DecimalField(decimal_places=4, default=0.24, max_digits=4),
        ),
    ]