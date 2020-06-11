from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User
from . models import Book, Review, Author

# Create your views here.

def dashboard(request):
    context={
        "logged_user": User.objects.get(id=request.session["user_id"]),
        "latest_reviews":Review.objects.all().order_by('-id')[:3],
        "books": Book.objects.all(),
    }
    return render (request, "dashboard.html", context)

def add_book(request):
    context={
        "authors": Author.objects.all(),
    }
    return render(request, "add_book.html", context)

def add_book_process(request):
    logged_user = User.objects.get(id=request.session["user_id"])
    if request.POST['new_author']:
        if Author.objects.filter(name=request.POST['new_author']).exists():
            messages.error(request, "Please select this existing author from the dropdown menu")
            return redirect("/books/add/")
        else:
            author = Author.objects.create(name = request.POST['new_author'])
    elif request.POST['existing_author'] == "":
            messages.error(request, "Please select an author")
            return redirect("/books/add/")
    else:
        author = Author.objects.get(id = request.POST['existing_author'])
    if Book.objects.filter(title__iexact=request.POST['title']).exists():
        messages.error(request,"This book already exists")
        return redirect ("/books/add/")
    else:
        new_book = Book.objects.create(author = author, title = request.POST['title'])
    new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], book = new_book, user=logged_user)

    return redirect (f"/books/{new_book.id}")

def book_reviews(request, book_id):
    context={
        "current_book":Book.objects.get(id = book_id),
        "logged_user":User.objects.get(id=request.session['user_id'])
    }
    return render(request, "book_reviews.html", context)

def add_review(request, book_id):
    logged_user = User.objects.get(id = request.session["user_id"])
    current_book = Book.objects.get(id = book_id)
    if request.POST['rating'] == '':
        messages.error(request, "Please enter a rating")
        return redirect(f"/books/{book_id}")
    if request.POST['content'] == "":
        messages.error(request, "Please enter a review")
        return redirect(f"/books/{book_id}")
    new_review = Review.objects.create(book= current_book, user = logged_user, content=request.POST['content'], rating = request.POST['rating'] )
    
    return redirect(f"/books/{book_id}")

def user_info(request, user_id):
    user = User.objects.get(id=user_id)
    total = len(user.has_reviewed.all())
    context={
        "user": user,
        "total_reviews":total
    }
    return render(request, "user_info.html", context)

def delete_review(request, review_id, current_book_id):
    Review.objects.get(id=review_id).delete()
    return redirect(f"/books/{current_book_id}")
