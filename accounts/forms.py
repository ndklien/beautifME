#For registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
<<<<<<< HEAD
from .models import GENDER_CHOICE, SKINCOND_CHOICE, SKINTYPE_CHOICE
=======
from functools import partial
from .models import UserAccount

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
>>>>>>> 095fb8ca72d7a430fb26576d9c1934e7dfa5adbe

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
<<<<<<< HEAD
        fields = ['username', 'email', 'password1', 'password2',
                  'fullName', 'birth', 'gender', 'skintype', 'skincondition', 'userImg']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class EditProfileForm(UserChangeForm):
    template_name='/change'

    class Meta:
        model = User
        fields = (
            'password',
        )
=======
        fields = ('username', 'email', 'first_name', 'last_name')
>>>>>>> 095fb8ca72d7a430fb26576d9c1934e7dfa5adbe
