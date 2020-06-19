from django.shortcuts import render, redirect
from login_app.models import User
from django.contrib import messages
import bcrypt,re

# Create your views here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def home(request):
    return render (request, "home.html")

def dashboard(request):
    context={
        "users": User.objects.all(),
        "logged_user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "dashboard.html", context)

def profile(request):
    context={
        "logged_user": User.objects.get(id=request.session['user_id']),

    }
    return render(request, "profile.html", context)

def update_info(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "Invalid email address.", extra_tags="email")
    result_email = User.objects.filter(email__iexact=(request.POST['email']))
    if len(result_email) > 0 and request.POST['email'] != logged_user.email:
        messages.error(request, "That email address is already registered.", extra_tags="email")
    if len(request.POST['first_name']) < 2:
        messages.error(request, "First name needs to be at least 2 characters long", extra_tags="first_name")
    if len(request.POST['last_name']) < 2:
        messages.error(request, "Last name needs to be at least 2 characters long", extra_tags="last-name")
    if messages:
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        logged_user.email = request.POST['email']
        logged_user.first_name = request.POST['first_name']
        logged_user.last_name = request.POST['last_name']
        logged_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_password(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    if len(request.POST['password']) < 8:
        messages.error(request, "Your password must be at least 8 characters long", extra_tags="password")
        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
    elif request.POST['password'] != request.POST['confirm_password']:
        messages.error(request, "Passwords don't match.", extra_tags="confirm")
        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
    else:
        password = request.POST['password']
        pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        logged_user.password = pswd_hash
        logged_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_description(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    logged_user.description = request.POST['description']
    logged_user.save()
    return redirect(request.META.get('HTTP_REFERER', "redirect_if_referer_not_found"))

