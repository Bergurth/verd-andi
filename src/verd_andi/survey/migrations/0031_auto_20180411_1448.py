# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-11 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0030_auto_20180306_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='store_owned_brand',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='item_pic_uploads/6b4a7f39-0802-4d08-a7c1-c7ac685ef24e'),
        ),
    ]
