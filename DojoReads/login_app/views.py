from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


# Create your views here.
def index(request):
    return render(request,"login.html")

def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(name = name, alias = alias, email = email, password = pswd_hash)
        request.session['user_id'] = user.id
    return redirect("/books/")

def login(request):
    user = User.objects.filter(email__iexact=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/books/")
        else:
            messages.error(request,"Incorrect e-mail or password")
            return redirect('/')
    else:
        messages.error(request, "Incorrect e-mail or password")
        return redirect ('/')

def logout(request):
    request.session.flush()
    return redirect('/')