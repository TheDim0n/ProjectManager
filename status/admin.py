from django.contrib import admin
from django import forms

from .models import Status
from . import fields


class StatusAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color', \
            'style': 'height: 100px; width: 100px;'})}
    }

admin.site.register(Status, StatusAdmin)
