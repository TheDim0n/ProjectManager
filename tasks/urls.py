from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('statuses', views.status_list, name='status_list'),
    path('new_status', views.create_status, name='create_status'),
    path('<int:task_id>', views.task_details, name="task_details")
]
