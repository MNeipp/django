from django.shortcuts import render, redirect, reverse, HttpResponse
from login_app.models import User
from django.contrib import messages
import bcrypt,re

# Create your views here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def home(request):
    return render (request, "home.html")

def dashboard(request):
    if "user_id" not in request.session:
        return redirect(reverse('register'))
    context={
        "users": User.objects.all(),
        "logged_user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "dashboard.html", context)

def profile(request):
    if "user_id" not in request.session:
        return redirect(reverse('register'))
    context={
        "logged_user": User.objects.get(id=request.session['user_id']),

    }
    return render(request, "profile.html", context)

def update_info(request):
    if request.method == "GET":
        return redirect(reverse('home'))
    logged_user = User.objects.get(id=request.session['user_id'])
    count = 0
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "Invalid email address.", extra_tags="email")
        count+=1
    result_email = User.objects.filter(email__iexact=(request.POST['email']))
    if len(result_email) > 0 and request.POST['email'] != logged_user.email:
        messages.error(request, "That email address is already registered.", extra_tags="email")
        count+=1
    if len(request.POST['first_name']) < 2:
        messages.error(request, "First name needs to be at least 2 characters long", extra_tags="first_name")
        count+=1
    if len(request.POST['last_name']) < 2:
        messages.error(request, "Last name needs to be at least 2 characters long", extra_tags="last-name")
        count+=1
    if count > 0:
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        logged_user.email = request.POST['email']
        logged_user.first_name = request.POST['first_name']
        logged_user.last_name = request.POST['last_name']
        logged_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_password(request):
    if request.method == "GET":
        return redirect(reverse('home'))
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
    if request.method == "GET":
        return redirect(reverse('home'))
    logged_user = User.objects.get(id=request.session['user_id'])
    logged_user.description = request.POST['description']
    logged_user.save()
    return redirect(request.META.get('HTTP_REFERER', "redirect_if_referer_not_found"))

def new_user(request):
    if "user_id" not in request.session:
        return redirect(reverse("home"))
    logged_user = User.objects.get(id=request.session['user_id'])
    if logged_user.user_level != 9:
        return redirect(reverse('dashboard'))
    else:
        return render(request, "add.html")

def edit_user(request, user_id):
    logged_user = User.objects.get(id=request.session['user_id'])
    if logged_user.user_level != 9:
        return redirect(reverse('dashboard'))
    else:
        context={
            "user": User.objects.get(id=user_id),
        }
        return render (request, "edit_user.html", context)


def edit_user_password(request, user_id):
    if request.method == "GET":
        return redirect(reverse('home'))
    else:
        edit_user = User.objects.get(id=user_id)
        if len(request.POST['password']) < 8:
            messages.error(request, "Your password must be at least 8 characters long", extra_tags="password")
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        elif request.POST['password'] != request.POST['confirm_password']:
            messages.error(request, "Passwords don't match.", extra_tags="confirm")
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        else:
            password = request.POST['password']
            pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            edit_user.password = pswd_hash
            edit_user.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def edit_user_info(request, user_id):
    if request.method == "GET":
        return redirect(reverse('home'))
    edit_user = User.objects.get(id=user_id)
    count=0
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "Invalid email address.", extra_tags="email")
        count+=1
    result_email = User.objects.filter(email__iexact=(request.POST['email']))
    if len(result_email) > 0 and request.POST['email'] != edit_user.email:
        messages.error(request, "That email address is already registered.", extra_tags="email")
        count+=1
    if len(request.POST['first_name']) < 2:
        messages.error(request, "First name needs to be at least 2 characters long", extra_tags="first_name")
        count+=1
    if len(request.POST['last_name']) < 2:
        messages.error(request, "Last name needs to be at least 2 characters long", extra_tags="last-name")
        count+=1
    if count > 0:
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        return HttpResponse("How the hell did you get here?")
    else:
        edit_user.email = request.POST['email']
        edit_user.first_name = request.POST['first_name']
        edit_user.last_name = request.POST['last_name']
        edit_user.user_level = request.POST['user_level']
        edit_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))