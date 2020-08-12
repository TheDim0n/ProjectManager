from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'finish_date', 'status', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter task title',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control form-control-sm',
                'type': 'date',
            }),
            'finish_date': forms.DateInput(attrs={
                'class': 'form-control form-control-sm',
                'type': 'date',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control no-markdown',
                'placeholder': 'Enter what to do in this task',
            }),
        }

class FilterForm(forms.Form):
    project = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}, ),
        label="Project:",
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'},),
        label="Status:",
    )
    