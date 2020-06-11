from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User
from . models import Book

# Create your views here.

def dashboard(request):
    context ={
        "user": User.objects.get(id=request.session["user_id"]),
        "books":Book.objects.all(),
    }

    return render(request,"dashboard.html", context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/books/')
    else:
        title = request.POST["book_title"]
        desc = request.POST["book_desc"]
        uploaded_by = User.objects.get(id=request.session["user_id"])
        new_book = Book.objects.create(title=title, desc=desc, uploaded_by=uploaded_by)
        new_book.liked_by.add(uploaded_by)

    return redirect("/books/")

def book_info(request, book_id):
    current_book = Book.objects.get(id=book_id)
    context={
        "book": current_book,
        "logged_user": User.objects.get(id=request.session["user_id"]),
        "users": User.objects.all(),
    }
    return render(request, "book_info.html", context)

def book_update(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f"/books/{book_id}/")
    else:
        updated_book = Book.objects.get(id=book_id)
        updated_book.title = request.POST["book_title"]
        updated_book.desc = request.POST["book_desc"]
        updated_book.save()
    return redirect(f"/books/{book_id}/")

def like_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session["user_id"])
    current_book.liked_by.add(user)
    return redirect(f"/books/")

def unlike_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session["user_id"])
    current_book.liked_by.remove(user)
    return redirect(f"/books/{book_id}/")

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect("/books/")

def user_info(request):
    context={
        "books":Book.objects.all(),
        "logged_user": User.objects.get(id=request.session["user_id"]),
    }
    return render(request, "user_info.html", context)