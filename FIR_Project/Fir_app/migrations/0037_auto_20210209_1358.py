# Generated by Django 3.1.4 on 2021-02-09 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0036_auto_20210209_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_station_data',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='police_station_data',
            name='longtitude',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='police_station_data',
            name='main_area',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fir',
            name='report_time',
            field=models.TimeField(default=datetime.time(13, 58, 56, 365271)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_end_time',
            field=models.TimeField(default=datetime.time(13, 58, 56, 364222)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_start_time',
            field=models.TimeField(default=datetime.time(13, 58, 56, 364222)),
        ),
    ]
