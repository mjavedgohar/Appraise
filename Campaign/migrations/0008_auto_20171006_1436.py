# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-06 21:36
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0007_auto_20171006_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='_str_name',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AddField(
            model_name='campaigndata',
            name='_str_name',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AddField(
            model_name='campaignteam',
            name='_str_name',
            field=models.TextField(blank=True, default='', editable=False),
        ),
    ]
