from django.shortcuts import render
from .models import Profile
from .forms import LoginForm, RegisterForm, EditProfile
from django.contrib.auth.models import User
from django.views import View

class LoginView(View):
    def get(self, request, args, kwargs):
        pass

