from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

from .models import Project
from .forms import ProjectForm


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create_project.html'

def index(request):
    projects_list = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects_list})

def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/details.html', {'project': project})
    