from django import forms

from .models import Project, Level


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task Title',
            })
        }
