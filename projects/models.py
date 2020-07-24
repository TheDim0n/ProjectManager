import datetime

from django.db import models
from status.models import Status
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=Status.objects.get_or_create(text="No status")[0].id,
    )
    description = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=Status.objects.get_or_create(text="No status")[0].id,
    )
    def __str__(self):
        return self.name
