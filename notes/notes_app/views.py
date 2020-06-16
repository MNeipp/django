from django.shortcuts import render, redirect, reverse
from .models import Note

# Create your views here.

def index(request):
    if request.method == 'POST':
        Note.objects.create(title = request.POST['title'],content=request.POST['content'])
        
        context={
            "notes":Note.objects.all()
        }
        return render (request, "notes_index.html", context)
    else:
        context={
            "notes":Note.objects.all()
        }
        return render (request, 'index.html', context)