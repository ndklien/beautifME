from django.shortcuts import render, redirect
from django.views import generic

#For registration
from .forms import RegisterForm

#For login and logout

# Create your views here.

#Registration function
def registration(request):
    if request.method == "POST":
        form = RegisterForm(request)
        if form.is_valid():
            form.save()
        
        return redirect('product/base_home.html')
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


# About us view

def aboutView(request):
    return render(request, 'accounts/about.html')