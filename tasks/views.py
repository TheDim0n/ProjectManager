from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from status.models import Status
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    ordering = ['finish_date']

    def get_context_data(self, *args, **kwargs):
        tasks = []
        if self.request.user.is_authenticated:
            tasks = Task.objects.filter(created_by=self.request.user)
        status_list = Status.objects.all()
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context['status_list'] = status_list
        context['tasks'] = tasks
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/details.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"


def task_status_ordered(request, status_name):
    status = Status.objects.get(text=status_name)
    sorted_task_list = Task.objects.filter(status=status.pk)
    status_list = Status.objects.all()
    context = {
        'tasks': sorted_task_list,
        'status_list': status_list,
    }
    return render(request, 'tasks/index.html', context)
