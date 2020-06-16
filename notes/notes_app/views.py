from django.shortcuts import render, redirect, reverse
from .models import Note

# Create your views here.

def index(request):
    if request.method == 'POST':
        Note.objects.create(title = request.POST['title'],content=request.POST['content'])
        return redirect(reverse("dashboard"))
    else:
        context={
            "notes":Note.objects.all()
        }
        return render (request, 'index.html', context)