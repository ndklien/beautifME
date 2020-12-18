from django.shortcuts import render, redirect

#For registration
from .forms import RegisterForm,LoginForm 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import User
#For login and logout

# Create your views here.

#Registration function
def registration(request):
    if request.method == "POST":
        form = RegisterForm(request)
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

    