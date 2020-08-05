from django.db import models

from . import fields

class Status(models.Model):

    text = models.CharField(max_length=200)
    color = fields.ColorField('Color', default='#FFFFFF')

    def text_color(self):
        color_hex = self.color[1:]
        is_dark = True
        for i in range(0, len(color_hex)-1, 2):
            tmp = color_hex[i] + color_hex[i + 1]
            if int(tmp, 16) > 150:
                is_dark = False
                break
        
        if is_dark:
            return '#EEEEEE'
        return '#111111'

    def __str__(self):
        return self.text
        