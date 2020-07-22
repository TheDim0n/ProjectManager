from django.db import models

from . import fields

class Status(models.Model):

    text = models.CharField(max_length=200)
    color = fields.ColorField('Color', default='#FFFFFF')

    def __str__(self):
        return self.text
        