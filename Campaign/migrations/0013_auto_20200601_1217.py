# Generated by Django 2.2.12 on 2020-06-01 12:17
from django.db import migrations
from django.db import models

import Campaign.models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0012_auto_20190705_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='batches',
            field=models.ManyToManyField(
                blank=True,
                related_name='campaign_campaign_batches',
                related_query_name='campaign_campaigns',
                to='Campaign.CampaignData',
                verbose_name='Batches',
            ),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='packageFile',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to='Packages',
                validators=[Campaign.models._validate_package_file],
                verbose_name='Package file',
            ),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='teams',
            field=models.ManyToManyField(
                blank=True,
                related_name='campaign_campaign_teams',
                related_query_name='campaign_campaigns',
                to='Campaign.CampaignTeam',
                verbose_name='Teams',
            ),
        ),
    ]