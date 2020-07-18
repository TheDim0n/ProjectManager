from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.task_details, name="task_details"),
    path('create_task', views.TaskCreateView.as_view(success_url='/tasks/'), name='create_task'),
    path('update_task/<int:pk>', views.TaskUpdateView.as_view(), name="update_task"),
]
