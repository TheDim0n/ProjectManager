from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse


from status.models import Status
from tasks.models import Task
from tasks.forms import TaskForm
from .models import Project, Level
from .forms import ProjectForm, LevelForm

class ProjectLevelUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/register'
    model = Level
    form_class = LevelForm
    template_name = "projects/level_details.html"

class ProjectLevelDeleteView(LoginRequiredMixin, DeleteView):
    model = Level
    template_name = "projects/delete_level.html"
    def get_success_url(self):
        return reverse('projects:project_details', args=str(self.object.project.id))

class ProjectTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "projects/delete_task.html"
    def get_success_url(self):
        return reverse('projects:project_details', args=str(self.object.level.project.id))

class ProjectTaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/register'
    model = Task
    form_class = TaskForm
    template_name = "projects/task_details.html"

class ProjectTaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/register'
    model = Task
    form_class = TaskForm
    template_name = 'projects/create_task.html'

    def form_valid(self, form):
        form.instance.level_id = self.kwargs['lpk']
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects:project_details', args=(self.kwargs['pk'],))


class ProjectLevelCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/register'
    model = Level
    form_class = LevelForm
    template_name = 'projects/create_level.html'
    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        form.instance.root_level_id = self.kwargs['lpk']
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects:project_details', args=(self.kwargs['pk'],))


class ProjectCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/register'
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create_project.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        zero_level = Level.objects.create_zero_level(self.object, self.request.user)
        zero_level.save()
        return HttpResponseRedirect(self.object.get_absolute_url())


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/index.html'
    ordering = ['name']

    def get_context_data(self, *args, **kwargs):
        projects = []
        if self.request.user.is_authenticated:
            projects = Project.objects.filter(created_by=self.request.user)
        status_list = Status.objects.all()
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context['status_list'] = status_list
        context['projects'] = projects
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['zero_level'] = Level.objects.get_zero(self.object)
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


def projects_status_ordered(request, status_name):
    if request.user.is_authenticated:
        status = Status.objects.get(text=status_name)
        sorted_project_list = Project.objects.filter(created_by=request.user, status=status.pk)
    else:
        sorted_project_list = []
    status_list = Status.objects.all()
    context = {
        'projects': sorted_project_list,
        'status_list': status_list,
    }
    return render(request, 'projects/index.html', context)

# class LevelsDetailView(ListView):
#     model = Level
#     form_class = LevelForm
#     template_name = "projects/levels.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     context['a'] = 5
    #     return context
