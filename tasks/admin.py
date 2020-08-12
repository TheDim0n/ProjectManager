from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'finish_date')

admin.site.register(Task, TaskAdmin)
