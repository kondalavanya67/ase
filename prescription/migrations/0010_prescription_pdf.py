# Generated by Django 2.1.2 on 2018-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0009_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media_/pdf/'),
        ),
    ]