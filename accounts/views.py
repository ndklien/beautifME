from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserAccount
#For registration

from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, profileForm
from django import forms

#For login and logout
from .forms import RegisterForm, profileForm

# Create your views here.

#Registration function
def registration(request):
    form = RegisterForm()
    message = ''

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Register succeed.'
        else:
            message = 'Register failed.'

    context = {
        "form": form,
        'message': message,
    }
    return render(request, 'accounts/register.html', context)
    

# Return website when logged out.
class LogoutView(generic.View):

    template_name = 'accounts/logout.html'

    def get(self, request):
        response = logout(request)
        return render(response, self.template_name)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'accounts/changepass_success.html')
        else:
            return render(request, 'accounts/change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

 
# View and Edit user Profile

def view_editProfile(request):
    # profile = request.user
    # profile.first_name = request.POST.get('first_name')
    # profile.last_name = request.POST.get('last_name')
    message = ''
    if request.method == 'POST':
        form = profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message = 'Save succeed.'
        else:
            message = 'Save failed.'
    else:
        form = profileForm(instance=request.user)
    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'accounts/accounts_preview.html', context)

def aboutView(request):
    return render(request, 'accounts/about.html')
    
