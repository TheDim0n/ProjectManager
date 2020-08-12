# Generated by Django 3.0.8 on 2020-08-10 14:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0001_initial'),
        ('projects', '0002_auto_20200810_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.datetime(2020, 8, 10, 14, 21, 0, 272668, tzinfo=utc))),
                ('finish_date', models.DateField(default=datetime.datetime(2020, 8, 11, 14, 21, 0, 272668, tzinfo=utc))),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.Level')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
        ),
    ]