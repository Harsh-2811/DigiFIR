# Generated by Django 2.2.17 on 2021-02-16 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0040_auto_20210211_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy_fir',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fir',
            name='report_time',
            field=models.TimeField(default=datetime.time(9, 54, 50, 215011)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_end_time',
            field=models.TimeField(default=datetime.time(9, 54, 50, 213016)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_start_time',
            field=models.TimeField(default=datetime.time(9, 54, 50, 213016)),
        ),
    ]
