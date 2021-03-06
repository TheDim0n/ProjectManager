import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from status.models import Status
from projects.models import Level


class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    description = models.TextField(max_length=10000, blank=True)
    level = models.ForeignKey(Level, related_name="tasks", on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tasks:task_details", args=[self.id])
    

    def check_expired(self):
        done_status = Status.objects.get(text="Done")
        expired_status = Status.objects.get_or_create(text="Expired", defaults={"color": "#8D1616"})[0]
        if self.status != done_status:
            if self.finish_date < timezone.localtime().date():
                Task.objects.filter(pk=self.id).update(status=expired_status)
            elif self.status == expired_status:
                Task.objects.filter(pk=self.id).update(status=Status.objects.get(text="No status"))
