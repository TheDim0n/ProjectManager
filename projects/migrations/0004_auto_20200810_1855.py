# Generated by Django 3.0.8 on 2020-08-10 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200810_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='finish_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 15, 55, 18, 634717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='level',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 15, 55, 18, 634717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='finish_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 15, 55, 18, 634717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 15, 55, 18, 634717, tzinfo=utc)),
        ),
    ]
