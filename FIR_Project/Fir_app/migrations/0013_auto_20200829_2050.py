# Generated by Django 3.0.5 on 2020-08-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0012_myuser_ref_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='ref_key',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]