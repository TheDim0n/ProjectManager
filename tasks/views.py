from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Status, Task
from .forms import NewStatus


def index(request):
    task_list = Task.objects.all()
    return render(request, 'tasks/index.html', {'task_list': task_list})

def status_list(request):
    __list = Status.objects.all()
    context = {
        'status_list': __list,
    }
    return render(request, 'tasks/statuses.html', context)

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/details.html', {'task': task})

def create_status(request):
    if request.method == 'POST':
        form = NewStatus(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_status = Status(text=text)
            new_status.save()
            return HttpResponseRedirect('/tasks/')
    else:
        form = NewStatus()
    return render(request, 'tasks/add_status.html', {'form': form})
