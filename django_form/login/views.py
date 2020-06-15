from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegistrationForm, LoginForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form2 = LoginForm(request.POST)
        if form.is_valid():
            return redirect(reverse('success'))
        elif form2.is_valid():
            return redirect(reverse('success'))

    else:
        reg_form = RegistrationForm()
        login_form = LoginForm()
        context = {
            "reg_form": reg_form,
            "login_form": login_form
        }
        return render (request, "index.html", context)

def success(request):
    return HttpResponse('<h1 style="color:green;">You did it!</h1>')