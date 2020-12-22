from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth import logout

#For registration
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm,LoginForm, EditProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

#For login and logout

# Create your views here.

#Registration function
def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = RegisterForm()
        context = {
        "form": form,
        }
        return render(request, 'accounts/register.html', context)
    
    
""" Return website when logged out."""
class LogoutView(generic.View):

    template_name = 'accounts/logout.html'

    def get(self, request):
        response = logout(request)
        return render(response, self.template_name)
