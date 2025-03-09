from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html' 
    success_url = reverse_lazy('signup')
    form_class = CustomUserCreationForm
