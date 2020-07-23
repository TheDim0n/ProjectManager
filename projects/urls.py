from django.urls import path

from . import views


app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>', views.project_details, name="project_details"),
    path('create_project', views.ProjectCreateView.as_view(success_url='/projects/'), name='create_project'),

]
