from django.db import models

class Status(models.Model):

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
        