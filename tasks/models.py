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
        default=Status.objects.get_or_create(text="No status")[0].id,
    )
    description = models.TextField(max_length=1000, blank=True)
    level = models.ForeignKey(Level, related_name="tasks", on_delete=models.PROTECT, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tasks:task_details", args=[self.id])

    def was_expired(self):
        done_status = Status.objects.get(text="Done")
        if self.status != done_status:
            if self.finish_date < timezone.now().date():
                self.status = Status.objects.get_or_create(
                    text="Expired",
                    defaults={"color": "#D10000"}
                )[0]
                self.save()
                return True
        return False
