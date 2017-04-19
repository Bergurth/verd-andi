# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('enName', models.CharField(max_length=200)),
                ('char_type', models.IntegerField()),
                ('isProperty', models.BooleanField(default=False)),
                ('specify', models.BooleanField(default=False)),
                ('value', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obeservation_number', models.IntegerField(blank=True)),
                ('obs_time', models.DateField()),
                ('shop_type', models.IntegerField()),
                ('shop_identifier', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=4)),
                ('discount', models.CharField(max_length=4)),
                ('value', models.DecimalField(decimal_places=4, max_digits=25)),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('observed_quantity', models.DecimalField(decimal_places=4, max_digits=25)),
                ('obs_comment', models.CharField(blank=True, max_length=300)),
                ('specified_characteristics', models.CharField(blank=True, max_length=400)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Item')),
                ('observer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_observer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, max_length=4)),
                ('dataflowID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Observation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Item'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]