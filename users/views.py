# from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse

from .forms import SignUpForm, ChangeForm

class UserCreationView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

class UserChangeView(generic.UpdateView):
    form_class = ChangeForm
    template_name = "registration/edit_profile.html"

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse('projects:index')