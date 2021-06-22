from django import forms
from django.forms import widgets
from .models import Proveedor, Plato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        