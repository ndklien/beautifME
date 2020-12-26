#For registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from functools import partial
from .models import UserAccount

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

#Add more fields in the Registration Form for User
# Registration Form 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class profileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
