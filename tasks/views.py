from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView

from .models import Task
from .forms import NewTask

def index(request):
    task_list = Task.objects.all()
    return render(request, 'tasks/index.html', {'task_list': task_list})

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/details.html', {'task': task})

# def create_task(request):
#     if request.method == 'POST':
#         form = NewTask(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             new_task = Task(text=text)
#             new_task.save()
#             return HttpResponseRedirect('/tasks/')
#     else:
#         form = NewTask()
#     return render(request, 'tasks/add_task.html', {'form': form})


class CreateTask(CreateView):
    form_class = NewTask
    template_name = 'tasks/add_task.html'
    succes_url = '/success/'
