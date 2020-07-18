from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from .models import Task
from .forms import NewTask

def index(request):
    task_list = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': task_list})

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/details.html', {'task': task})

class TaskCreateView(CreateView):
    model = Task
    form_class = NewTask
    template_name = 'tasks/create_task.html'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = NewTask
    template_name = "tasks/update_task.html"
