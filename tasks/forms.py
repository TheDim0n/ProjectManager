from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'finish_date', 'status', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task Title',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'finish_date': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter what to do in this task',
            }),
        }
