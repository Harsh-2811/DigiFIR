# Generated by Django 3.1.4 on 2021-02-08 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0025_auto_20210208_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='position',
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='atitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='report_time',
            field=models.TimeField(default=datetime.time(20, 39, 32, 701960)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_end_time',
            field=models.TimeField(default=datetime.time(20, 39, 32, 700962)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_start_time',
            field=models.TimeField(default=datetime.time(20, 39, 32, 700962)),
        ),
    ]