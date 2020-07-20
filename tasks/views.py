from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'

class TaskDetailView(DetailView):
    model = Task
    # context_object_name = 'task'
    template_name = 'tasks/details.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
