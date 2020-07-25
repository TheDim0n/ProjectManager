import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone, dateformat

from status.models import Status
from tasks.forms import TaskForm
from .models import Project
from .forms import ProjectForm, LevelForm


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create_project.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/index.html'
    ordering = ['name']

    def get_context_data(self, *args, **kwargs):
        projects = []
        if self.request.user.is_authenticated:
            projects = Project.objects.all()
            # Project.objects.filter(created_by=self.request.user)
        status_list = Status.objects.all()
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context['status_list'] = status_list
        context['projects'] = projects
        return context

def projects_status_ordered(request, status_name):
    status = Status.objects.get(text=status_name)
    sorted_project_list = Project.objects.filter(status=status.pk)
    status_list = Status.objects.all()
    context = {
        'projects': sorted_project_list,
        'status_list': status_list,
    }
    return render(request, 'projects/index.html', context)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['task_form'] = TaskForm
        context['level_form'] = LevelForm
        return context

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/register'
    model = Project
    form_class = ProjectForm
    template_name = "projects/update_project.html"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "tasks/delete_project.html"
    