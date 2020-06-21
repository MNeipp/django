from django.shortcuts import render, redirect, reverse, HttpResponse
from login_app.models import User
from django.contrib import messages
from .models import Post, Comment
import bcrypt

# Create your views here.

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
    errors = User.objects.info_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        logged_user = User.objects.get(id=request.session["user_id"])
        logged_user.email = request.POST['email']
        logged_user.first_name = request.POST['first_name']
        logged_user.last_name = request.POST['last_name']
        logged_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_password(request):
    if request.method == "GET":
        return redirect(reverse('home'))
    errors = User.objects.password_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        logged_user = User.objects.get(id=request.session['user_id'])
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
    if "user_id" not in request.session:
        return redirect(reverse('home'))
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
    errors = User.objects.password_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        edit_user = User.objects.get(id=user_id)
        password = request.POST['password']
        pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        edit_user.password = pswd_hash
        edit_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def edit_user_info(request, user_id):
    if request.method == "GET":
        return redirect(reverse('home'))
    errors = User.objects.info_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        edit_user = User.objects.get(id=user_id)
        edit_user.email = request.POST['email']
        edit_user.first_name = request.POST['first_name']
        edit_user.last_name = request.POST['last_name']
        edit_user.user_level = request.POST['user_level']
        edit_user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def message_board(request, user_id):
    if "user_id" not in request.session:
        return redirect(reverse("home"))
    context={
        "logged_user":User.objects.get(id=request.session["user_id"]),
        "all_users":User.objects.all(),
        "user":User.objects.get(id=user_id),
    }
    return render(request, "message_board.html",context)

def make_post(request, user_id):
    if request.method == "GET":
        return redirect(reverse("home"))
    else:
        logged_user = User.objects.get(id=request.session["user_id"])
        user_board = User.objects.get(id=user_id)
        Post.objects.create(content = request.POST["message"], creator = logged_user, board=user_board)

    context={
        "user": user_board,
    }
    return render(request, "ajax_message_board.html", context)

def make_comment(request, post_id):
    if request.method == "GET":
        return redirect(reverse("home"))
    else:
        logged_user = User.objects.get(id=request.session["user_id"])
        current_post = Post.objects.get(id=post_id)
        Comment.objects.create(content = request.POST["comment"], creator = logged_user, post=current_post)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def delete_user(request, user_id):
    if request.method == "GET":
        return redirect(reverse("logout"))
    logged_user = User.objects.get(id=request.session['user_id'])
    if logged_user.user_level != 9:
        return redirect(reverse("logout"))
    else:
        user_to_delete = User.objects.get(id=user_id)
        user_to_delete.delete()
        return redirect(reverse('dashboard'))