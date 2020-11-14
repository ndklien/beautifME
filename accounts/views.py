from django.shortcuts import render, redirect

#For registration
from .forms import RegisterForm

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
