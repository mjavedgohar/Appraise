# Generated by Django 3.2.12 on 2022-08-01 04:11
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0049_auto_20220629_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directassessmentdocumentresult',
            options={},
        ),
        migrations.AddField(
            model_name='directassessmentdocumentresult',
            name='errors',
            field=models.TextField(
                blank=True,
                help_text='(max. 2000 characters)',
                max_length=2000,
                null=True,
                verbose_name='Errors',
            ),
        ),
    ]