import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse

from status.models import Status
# from projects.models import Level


class Task(models.Model):

    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    description = models.TextField(max_length=1000, blank=True)
    # level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tasks:task_details", args=[self.id])
