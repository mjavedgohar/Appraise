# Generated by Django 2.1.5 on 2019-05-27 08:04
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0036_auto_20190524_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpair',
            name='sourceText',
            field=models.TextField(blank=True, verbose_name='Source text'),
        ),
        migrations.AlterField(
            model_name='textpair',
            name='targetText',
            field=models.TextField(blank=True, verbose_name='Target text'),
        ),
    ]
