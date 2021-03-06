# Generated by Django 3.1.4 on 2021-02-09 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0037_auto_20210209_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police_station_data',
            name='longtitude',
        ),
        migrations.AddField(
            model_name='police_station_data',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='report_time',
            field=models.TimeField(default=datetime.time(14, 7, 13, 551986)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_end_time',
            field=models.TimeField(default=datetime.time(14, 7, 13, 550869)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_start_time',
            field=models.TimeField(default=datetime.time(14, 7, 13, 550869)),
        ),
        migrations.AlterField(
            model_name='police_station_data',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=30, null=True),
        ),
    ]
