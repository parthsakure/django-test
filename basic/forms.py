from attr import fields
from django import forms
from django.contrib.auth.models import User
from basic.models import UserModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['portfolio', 'dp']