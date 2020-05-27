from django.shortcuts import render, HttpResponse, redirect
from books_authors_app.models import Book, Author

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = {
        "all_books":all_books  
    }
    return render(request,"index.html", context)

def book_info(request, book_ID):
    current_book = Book.objects.get(id=book_ID)
    all_authors = Author.objects.all()
    not_authors = Author.objects.exclude(books__id=book_ID)
    context = {
        "book_ID": book_ID,
        "current_book":current_book,
        "all_authors": all_authors,
        "not_authors":not_authors,
    }
    return render(request,"book_info.html", context)

def authors(request):
    all_authors = Author.objects.all()
    context={
        "all_authors":all_authors
    }
    return render(request, "authors.html", context)

def author_info(request,author_ID):
    current_author = Author.objects.get(id=author_ID)
    all_books = Book.objects.all()
    not_books = Book.objects.exclude(authors__id=author_ID)
    context = {
        "author_ID" : author_ID,
        "current_author":current_author,
        "all_books":all_books,
        "not_books":not_books,
    }
    return render(request, "author_info.html", context)

def add_book(request):
    if request.method == "POST":
        title= request.POST['title']
        desc = request.POST['desc']
        new_book = Book.objects.create(title=title, desc=desc)
        new_book.save()
    return redirect('/')

def add_author(request):
    if request.method == "POST":
        first = request.POST['first_name']
        last = request.POST['last_name']
        notes = request.POST['notes']
        new_author = Author.objects.create(first_name=first, last_name=last, notes=notes)
        new_author.save()
    return redirect('/authors')

def add_work(request, author_ID):
    if request.method == "POST":
        data = request.POST.copy()
        current_book = Book.objects.get(title=data['works'])
        current_author = Author.objects.get(id=author_ID)
        current_author.books.add(current_book)
    return redirect(f'/authors/{current_author.id}')


def add_contributing_author(request, book_ID):
    if request.method == "POST":
        data= request.POST.copy()
        current_book = Book.objects.get(id=book_ID)
        current_author = Author.objects.get(last_name=data['contributing_author'])
        current_book.authors.add(current_author)
    return redirect(f'/books/{current_book.id}')
