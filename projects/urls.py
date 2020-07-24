from django.urls import path

from . import views


app_name = 'projects'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('<int:project_id>', views.project_details, name="project_details"),
    path('create_project', views.ProjectCreateView.as_view(success_url='/projects/'), name='create_project'),
    path('status/<str:status_name>', views.projects_status_ordered, name="status_order"),
]
