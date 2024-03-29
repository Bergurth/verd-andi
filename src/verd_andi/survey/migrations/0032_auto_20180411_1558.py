# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-11 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0031_auto_20180411_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='store_owned_brand',
            new_name='shop_own_brand',
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='item_pic_uploads/6d81637f-6f80-43ef-b56f-61491c7c98cf'),
        ),
    ]
