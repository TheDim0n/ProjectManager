from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.UserCreationView.as_view(), name='register'),
    path('edit_profile/', views.UserChangeView.as_view(), name='edit_profile'),
]
