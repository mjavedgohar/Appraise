# Generated by Django 2.1.5 on 2019-02-28 16:26
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0032_auto_20190228_0821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskagenda',
            options={'permissions': (('reset_taskagenda', 'Can reset task agendas'),)},
        ),
    ]