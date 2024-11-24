from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class SignUp(UserCreationForm):
    email = forms.EmailField (label="Email", required=True, widget=forms.TextInput(attrs={"type":"email", "placeholder":"Email"}))
    first_name = forms.CharField(max_length=100, label="", required=True, widget=forms.TextInput(attrs={"type":"text", "placeholder":"First Name"}))
    last_name = forms.CharField(max_length=100, label="",required=True, widget=forms.TextInput(attrs={"type":"text", "placeholder":"Last Name"}))
    password1 = forms.CharField(label="Enter password", required=True, widget=forms.PasswordInput(attrs={"type":"password", "placeholder":"*********"}))
    password2 = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput(attrs={"type":"password", "placeholder":"*********"}))
    
    class Meta:
        model = Account
        fields =[
            'email','first_name','last_name' ,'password1', 'password2'
        ]
