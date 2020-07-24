from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from status.models import Status
from .models import Project
from .forms import ProjectForm


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

def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/details.html', {'project': project})

    