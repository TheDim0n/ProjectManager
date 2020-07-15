from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Status
from .forms import NewStatus


def index(request):
    return render(request, 'tasks/index.html')

def status_list(request):
    __list = Status.objects.all()
    context = {
        'status_list': __list,
    }
    return render(request, 'tasks/statuses.html', context)

def create_status(request):
    if request.method == 'POST':
        form = NewStatus(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_status = Status(text=text)
            new_status.save()
            return HttpResponseRedirect('/tasks/')
    else:
        form = NewStatus()
    return render(request, 'tasks/add_status.html', {'form': form})
