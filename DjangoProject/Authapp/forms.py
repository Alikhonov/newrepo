from django import forms
from Authapp.models import UserInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields={'username','email','password'}

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = {'profile_pics','Portfolio'}
