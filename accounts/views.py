from django.shortcuts import render, redirect

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
        
        return redirect('product/base.html')
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])

            if user is not None:
                login(request, user)
                return render(request, 'product/base_home.html',{'user': user})
            else:
                return HttpResponse('Fail! Please try again!')

    else: 
        form = LoginForm()
    
    return render(request, 'accounts/login.html',{'form': form})

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

    