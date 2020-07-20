from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('<int:pk>', views.TaskDetailView.as_view(), name="task_details"),
    path('create_task', views.TaskCreateView.as_view(success_url='/tasks/'), name='create_task'),
    path('update_task/<int:pk>', views.TaskUpdateView.as_view(), name="update_task"),
    path('delete_task/<int:pk>', views.TaskDeleteView.as_view(success_url='/tasks/'), name="delete_task"),
    path('status/<str:status_name>', views.task_status_oredered, name="status_order"),
]
