from django.shortcuts import render, redirect

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
        
        return redirect('product/base.html')
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, 'product/base_home.html', context)
