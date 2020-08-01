from django import forms

from projects.models import Project
from status.models import Status

from .models import Task

PROJECTS = [("All", "All")]
for item in Project.objects.all():
    PROJECTS.append((item.name, item.name))


STATUSES = [("All", "All")]
for item in Status.objects.all():
    STATUSES.append((item.text, item.text))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'finish_date', 'status', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'finish_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter what to do in this project',
            }),
        }

class FilterForm(forms.Form):
    project = forms.Field(
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}, choices=PROJECTS),
        label="Project:",
    )
    status = forms.Field(
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}, choices=STATUSES),
        label="Status:",
    )
