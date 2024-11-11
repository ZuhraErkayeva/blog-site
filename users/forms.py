from django import forms


class BaseUserForm(forms.Form):
    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    avatar = forms.ImageField()
    email = forms.EmailField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class RegisterForm(BaseUserForm):
    password1 = forms.CharField()
    password2 = forms.CharField()


class EditProfile(BaseUserForm):
    old_password = forms.CharField()
    new_password = forms.CharField()
