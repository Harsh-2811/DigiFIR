# Generated by Django 3.1.4 on 2021-02-09 03:32

import datetime
from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0033_auto_20210209_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.AlterField(
            model_name='fir',
            name='report_time',
            field=models.TimeField(default=datetime.time(9, 2, 57, 74930)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_end_time',
            field=models.TimeField(default=datetime.time(9, 2, 57, 73931)),
        ),
        migrations.AlterField(
            model_name='police_data',
            name='duty_start_time',
            field=models.TimeField(default=datetime.time(9, 2, 57, 73931)),
        ),
    ]
