from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from braces.views import AnonymousRequiredMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserPasswordReset, CustomUserChangeForm


class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/login.html'


class SignUpView(AnonymousRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'
