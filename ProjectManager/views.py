from django.shortcuts import render

from tasks.models import Task


def start_page(request):
    task_list = Task.objects.all()
    return render(request, 'start_page.html', {'tasks': task_list})
