from django.db import models
#from tasks.models import Status


class Project(models.Model):
    name = models.CharField(max_length=100)
    # status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name



class Level(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    # status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
