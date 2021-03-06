# Generated by Django 3.0.5 on 2020-08-26 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fir_app', '0010_city_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fir_app.city'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fir_app.states'),
        ),
    ]
