import datetime

from django.db import models
from django.utils import timezone


class Status(models.Model):

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Task(models.Model):

    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
