from django import forms

from .models import Project, Level

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
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
                'class': 'form-control no-markdown',
                'placeholder': 'Enter what to do in this project',
            }),

        }
        
class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['name', 'start_date', 'finish_date', 'status', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stage title',
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
                'class': 'form-control no-markdown',
                'placeholder': 'Enter what to do on this group (stage)',
            }),

        }
