from django.forms import ModelForm

from .models import Task
# class NewTask(forms.Form):
#     text = forms.CharField(label='Name', max_length=200)
class NewTask(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'finish_date', 'status', 'description']
