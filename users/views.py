from audioop import reverse
from importlib.metadata import files

from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from .models import Profile, UserToken
from .forms import LoginForm, RegisterForm, EditProfile
from django.contrib.auth.models import User
from django.views import View


class HomeWithoutLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request,'users/index-without-login.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'users/login.html')

    def post(self, request, *args, **kwargs):
        print(request.POST.get('email'))
        print(request.POST.get('password'))


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'users/register.html')

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] != cd['password2']:
                return redirect('users:register')
            try:
                user = User.objects.create_user(
                    username=cd['username'],
                    email=cd['email']
                )
                user.first_name = cd['name']
                user.set_password(cd['password1'])
                user.save()
                user_profile = get_object_or_404(Profile, user=user)
                user_profile.profile_image = cd['avatar']
                user_profile.save()
                user_token = UserToken.objects.create(user=user)
                reversed_link = reverse('users:verify_email', args=[user_profile.pk, user_token.token])
                message = f"Assalom alaykum {user.first_name}, akauntingzni tasdiqlash uchun quyidagi havolga kiring:\n{reversed_link}"
                send_mail(
                    subject="Blog saytdan tasdiqlash",
                    message=message,
                    from_email='zuhraerkayeva7@gmail.com',
                    recipient_list=[user.email],
                )
            except IntegrityError:
                form_error = "A user with that username or email already exists."
        return render(request, 'users/register.html', {'form': form, 'form_error': form_error})


class VerifyEmail(View):
    def get(self, request, pk, token, *args, **kwargs):
        user_profile = get_object_or_404(Profile, pk=pk)
        user_token = get_object_or_404(UserToken, user=user_profile)
        user_profile.is_email_verified = True
        user_profile.save()
        return redirect('users:login')



class ProfileUpdateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        pass


class MyProfile(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

