# Generated by Django 2.2 on 2019-04-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0008_auto_20190403_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='icd_type',
            field=models.IntegerField(default=10, verbose_name='ICD Type'),
        ),
    ]
