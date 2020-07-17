from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.task_details, name="task_details")
]
