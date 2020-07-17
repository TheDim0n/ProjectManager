from django.shortcuts import render, get_object_or_404

from .models import Task

def index(request):
    task_list = Task.objects.all()
    return render(request, 'tasks/index.html', {'task_list': task_list})

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/details.html', {'task': task})
