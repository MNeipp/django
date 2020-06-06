from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request,"home.html")

def success(request):
    context = {
        "name": request.session['name']
    }
    return render(request,"success.html", context)

def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        DOB = request.POST['DOB']
        password = request.POST['password']
        pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        request.session['name'] = first_name
        User.objects.create(first_name = first_name, last_name = last_name, email = email, DOB=DOB ,password = pswd_hash)
    return redirect("/success/")

def login(request):
    user = User.objects.filter(email__iexact=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            print(logged_user.first_name)
            request.session['name'] = logged_user.first_name
            return redirect("/success")
        else:
            messages.error(request,"Incorrect e-mail or password")
            return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')