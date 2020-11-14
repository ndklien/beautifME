#For registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import addAccountsForm, GENDER_CHOICE, SKINCOND_CHOICE, SKINTYPE_CHOICE

#Add more fields in the Registration Form for User
class RegisterForm(UserCreationForm):
    #user email
    email = forms.EmailField()

    #user fullname
    fullName = forms.CharField(max_length=50)

    #user gender: call choices from accounts.models.py
    gender = forms.CharField(max_length=2, widget=forms.Select(choices=GENDER_CHOICE))

    #user date of birth
    birth = forms.DateField()

    #user skintype
    skintype = forms.CharField(max_length=5, widget=forms.Select(choices=SKINTYPE_CHOICE))

    #user skin condition
    skincondition = forms.CharField(max_length=5, widget=forms.Select(choices=SKINCOND_CHOICE))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'fullName', 'birth']
