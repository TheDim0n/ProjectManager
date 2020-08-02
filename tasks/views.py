from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from status.models import Status
from .models import Task
from .forms import TaskForm, FilterForm


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    ordering = ['finish_date']

    def get_context_data(self, *args, **kwargs):
        try:
            project_name = self.request.GET['project']
        except KeyError:
            project_name = ''

        try:
            status_name = self.request.GET['status']
        except KeyError:
            status_name = ''

        last_initial = {
            'status': status_name,
            'project': project_name,
        }
    
        if self.request.user.is_authenticated:
            tasks = Task.objects.filter(created_by=self.request.user)
            if project_name and project_name != "All":
                tasks = tasks.filter(level__project__name=project_name)
            if status_name and status_name != "All":
                tasks = tasks.filter(status__text=status_name)
        status_list = Status.objects.all()
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context['status_list'] = status_list
        context['tasks'] = tasks
        context['filter_form'] = FilterForm(initial=last_initial)
        context['task_form'] = TaskForm
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/details.html'

    def get_context_data(self, *args, **kwargs):
        initial_content = {
            'name': self.object.name,
            'start_date': self.object.start_date,
            'finish_date': self.object.finish_date,
            'status': self.object.status,
            'description': self.object.description,
        }
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        context['task_form'] = TaskForm(initial=initial_content)
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/register'
    model = Task
    form_class = TaskForm
    template_name = 'tasks/index.html'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/register'
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
