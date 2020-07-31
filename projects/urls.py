from django.urls import path

from . import views


app_name = 'projects'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('<int:pk>', views.ProjectDetailView.as_view(), name="project_details"),
    path('create_project', views.ProjectCreateView.as_view(success_url='/projects/'), name='create_project'),
    path('status/<str:status_name>', views.projects_status_ordered, name="status_order"),
    path('update_project/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('<int:pk>/delete', views.ProjectDeleteView.as_view(success_url='/projects/'), name='delete_project'),
    path('<int:pk>/<int:lpk>/create_level', views.ProjectLevelCreateView.as_view(), name='create_level'),
    path('<int:pk>/<int:lpk>/create_task', views.ProjectTaskCreateView.as_view(), name='create_task'),
]
