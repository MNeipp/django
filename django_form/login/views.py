from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form2 = LoginForm(request.POST)
        
        if form.is_valid():
            request.session['name'] = request.POST['first_name']
            return redirect(reverse('success'))
        # elif form2.is_valid():
        #     return redirect(reverse('success'))
        else:
            context = {
                "reg_form": form,
                "login_form": form2
        }
            return render(request, 'index.html', context)

    else:
        reg_form = RegistrationForm()
        login_form = LoginForm()
        context = {
            "reg_form": reg_form,
            "login_form": login_form
        }
        return render (request, "index.html", context)

def success(request):
    return HttpResponse(f"<h1 style='color:green;'>You did it,{request.session['name']}</h1>")