from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('statuses', views.status_list, name='status_list'),
]
