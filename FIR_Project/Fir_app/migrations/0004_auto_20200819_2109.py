# Generated by Django 3.0.5 on 2020-08-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0003_myuser_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='userdata',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
