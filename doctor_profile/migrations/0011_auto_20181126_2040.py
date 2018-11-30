# Generated by Django 2.0.5 on 2018-11-26 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0010_auto_20181125_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='slot1',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='slot2',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='slot3',
        ),
        migrations.AddField(
            model_name='slot',
            name='start_time',
            field=models.CharField(blank=True, choices=[('09:00:00', '6 am'), ('12:00:00', '12 pm'), ('04:00:00', '4 pm')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdate',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]