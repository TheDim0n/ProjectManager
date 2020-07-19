from django.urls import path

from .views import UserCreationView


app_name = 'users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', UserCreationView.as_view(), name='register'),
]
