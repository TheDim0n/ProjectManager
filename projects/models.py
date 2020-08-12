import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from status.models import Status



class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    description = models.TextField(max_length=1000, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:project_details", args=[self.id])


class LevelManager(models.Manager):
    def create_zero_level(self, project_id, user_id):
        level = self.create(project=project_id, status=project_id.status, is_zero=True, created_by=user_id)
        return level

    def get_zero(self, project_id):
        return super().get(is_zero=True, project=project_id)



class Level(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    finish_date = models.DateField(default=timezone.now() + datetime.timedelta(days=1))
    project = models.ForeignKey(Project, related_name="levels", on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    is_zero = models.BooleanField(default=False, blank=True)
    root_level = models.ForeignKey("self", related_name="levels", on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    description = models.TextField(max_length=1000, blank=True)

    def get_absolute_url(self):
        return reverse("projects:level_details", args=[self.id])

    objects = LevelManager()
