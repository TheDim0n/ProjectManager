from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NewStatus
from .models import Status

# Create your views here.
def index(request):
    return render(request, 'status/index.html')

def status_list(request):
    __list = Status.objects.all()
    context = {
        'status_list': __list,
    }
    return render(request, 'status/statuses.html', context)

def create_status(request):
    if request.method == 'POST':
        form = NewStatus(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_status = Status(text=text)
            new_status.save()
            return HttpResponseRedirect('/status/')
    else:
        form = NewStatus()
    return render(request, 'status/add_status.html', {'form': form})
