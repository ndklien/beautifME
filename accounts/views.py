from django.contrib.messages.api import success
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
from django.contrib import messages

#For login and logout
from .forms import RegisterForm, profileForm

# Create your views here.

#Registration function
def registration(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register succeed!")
        else:
            messages.success(request, "Register failed!")

    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)
    

# Return website when logged out.
class LogoutView(generic.View):

    # template_name = 'accounts/logout.html'

    def get(self, request):
        response = logout(request)
        
        return redirect('homepage')
        # return render(response, self.template_name)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Change password succeed!")
        else:
            form = PasswordChangeForm(user=request.user)
            messages.success(request, "Change password failed!")
    else:
        form = PasswordChangeForm(user=request.user)

    args = {
        'form': form, 
    }
    return render(request, 'accounts/change_password.html', args)

 
# View and Edit user Profile

def view_editProfile(request):
    if request.method == 'POST':
        form = profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Save succeed.")
        else:
            messages.success(request, "Save failed!")
    else:
        form = profileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/accounts_preview.html', context)

def aboutView(request):
    return render(request, 'accounts/about.html')
    
