from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import User
import bcrypt
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form2 = LoginForm(request.POST)
        if request.POST.get('submit') == 'Register':
            # if form.is_valid():
            #     password = request.POST['password']
            #     pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            #     new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password=pswd_hash)
            #     request.session['user_id'] = new_user.id
            #     return redirect(reverse('success'))
            return HttpResponse("you registered")
        
        elif request.POST.get('submit') == 'Login':
            return HttpResponse("You suck")

        # else:
        #     context = {
        #         "reg_form":form,
        #         "login_form": form2
        # }
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
    logged_user = User.objects.get(id=request.session['user_id'])
    name = logged_user.first_name
    return HttpResponse(f"<h1 style='color:green;'>You did it,{name}</h1>")