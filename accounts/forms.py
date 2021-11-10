from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, \
    ReadOnlyPasswordHashField
from .models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.CharField(max_length=50, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email...'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password...'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password...'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-enter password...'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'password1', 'password2', 'email']
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail....'}),
        }


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="Password", widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password')


class CustomUserPasswordReset(PasswordResetForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = CustomUser
        fields = ['email', ]
