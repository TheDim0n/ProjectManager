from django.http import HttpResponse
from django.shortcuts import render

from .models import Status


def index(request):
    return HttpResponse('Works!')

def status_list(request):
    __list = Status.objects.all()
    context = {
        'status_list': __list,
    }
    return render(request, 'tasks/statuses.html', context)
