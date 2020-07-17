# Generated by Django 3.0.8 on 2020-07-17 08:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200717_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 18, 8, 23, 10, 329784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 17, 8, 23, 10, 329755, tzinfo=utc)),
        ),
    ]
