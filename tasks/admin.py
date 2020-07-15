from django.contrib import admin

from .models import Status, Task


admin.site.register([Status, Task])
