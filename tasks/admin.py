from django.contrib import admin

from .models import Status, Task


admin.site.register(Task)
admin.site.register(Status)
