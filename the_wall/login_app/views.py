from django.shortcuts import render, redirect
from django.contrib import messages
from wall_app.models import Message, Comment
from .models import User
import datetime
import bcrypt


# Create your views here.
def index(request):
    return render(request,"home.html")

def success(request):
    today=datetime.datetime.today()
    context = {
        "user": User.objects.get(id=request.session["user_id"]),
        "messages": Message.objects.all(),
        "comments": Comment.objects.all(),
        "time_limit": today - datetime.timedelta(minutes=15)
    }
    return render(request,"wall.html", context)

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
        user = User.objects.create(first_name = first_name, last_name = last_name, email = email, DOB=DOB ,password = pswd_hash)
        request.session['user_id'] = user.id
    return redirect("/wall/")

def login(request):
    user = User.objects.filter(email__iexact=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/wall/")
        else:
            messages.error(request,"Incorrect e-mail or password")
            return redirect('/')
    else:
        messages.error(request, "Incorrect e-mail or password")
        return redirect ('/')

def logout(request):
    request.session.flush()
    return redirect('/')