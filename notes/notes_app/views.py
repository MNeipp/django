from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Note
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def update_content(request, note_id):
    if request.method == "POST":
        note = Note.objects.get(id=note_id)
        note.content = request.POST['content']
        note.save()
        context={
        "notes":Note.objects.all()
        }
        return render (request, 'notes_index.html', context)


@csrf_exempt
def delete_note(request, note_id):
    if request.method == "POST":
        Note.objects.get(id=note_id).delete()
        context ={
            "notes": Note.objects.all()
        }
        return render(request, 'notes_index.html', context)
