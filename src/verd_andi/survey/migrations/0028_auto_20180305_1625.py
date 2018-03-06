# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-05 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0027_auto_20180305_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='item_pic_uploads/8f89a224-f999-4c16-834c-2e87203bda62'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='discount',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='observation',
            name='flag',
            field=models.CharField(choices=[('E', 'E'), ('O', 'O')], max_length=4),
        ),
    ]
