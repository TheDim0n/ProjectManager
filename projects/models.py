import datetime

from django.db import models
from status.models import Status
from django.utils import timezone
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse("projects:project_details", args=[self.id])


class LevelManager(models.Manager):
    def create_zero_level(self, project_id):
        level = self.create(project=project_id, is_zero=True)
        return level

    def get_zero(self, project_id):
        return super().get(is_zero=True, project=project_id)



class Level(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    project = models.ForeignKey(Project, related_name="levels", on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=Status.objects.get_or_create(text="No status")[0].id,
    )
    is_zero = models.BooleanField(default=False, blank=True)
    root_level = models.ForeignKey("self", related_name="levels", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    description = models.TextField(max_length=1000, blank=True)

    objects = LevelManager()


